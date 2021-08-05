import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--year',help= 'Year for config to run with', default='2018')
parser.add_argument('--tarball',help= 'Inset name of tarball, only need for --gen', default='')
parser.add_argument('--folder_name',help= 'Inset name of dcache folder', default='betaRd33_0_mU2_gU3')
parser.add_argument("--gen", action='store_true',help="Run GEN-SIM")
parser.add_argument("--premix", action='store_true',help="Run premix")
parser.add_argument("--aod", action='store_true',help="Run AOD")
parser.add_argument("--miniaod", action='store_true',help="Run MINIAOD")
parser.add_argument("--dry_run", action='store_true',help="Will create files but not run them")
parser.add_argument("--run_all", action='store_true',help="Will run all tar.xz files in current directory")
parser.add_argument('--skip',help= 'If running with --run_all will skip this tarball', default='')
args = parser.parse_args()


def ReadReplaceAndWrite(template,filename,tarball_name,folder_name,add_tasks=False,lines_to_add=[],nevents=None):
  # Read in the file
  with open(template, 'r') as file :
    filedata = file.read()
  
  # Replace the target string
  filedata = filedata.replace('TARBALL_FILENAME',tarball_name).replace('SAMPLE_FILENAME',folder_name)

  if nevents != None: filedata = filedata.replace("N_EVENTS",str(nevents))

  if add_tasks:
    add_lines='tasks=list()\n'
    for i in lines_to_add:
      add_lines += "    "+i+"\n"
    filedata = filedata.replace("tasks=list()",add_lines)

  # Write the file out again
  with open(filename, 'w') as file:
    file.write(filedata)

def get_dataset(folder,ps,cl):
  ps = ps.upper()
  year = args.year
  if ps == "gensim":
    os.system("crab status %(cl)s/%(folder)s_%(ps)s_%(year)s/crab_%(folder)s_%(ps)s_%(year)s >> crab_status_output.txt" % vars())
  else:
    os.system("crab status %(cl)s/crab_%(folder)s_%(year)s_%(ps)s >> crab_status_output.txt" % vars())
  crab_status_file = open('crab_status_output.txt', 'r')
  for line in crab_status_file:
    if "Output dataset:" in line:
      output_dataset = line.split("Output dataset:")[1].strip()
  os.system("rm crab_status_output.txt")
  return output_dataset


if args.tarball == "":
  args.tarball = args.folder_name + "_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz"


if args.gen: 
  mn = "gen"
elif args.premix: 
  mn = "premix"
  ps = "gensim"
  cl = "./"
elif args.aod: 
  mn = "aod"
  ps = "premix"
  cl = "PREMIX"
elif args.miniaod: 
  mn = "miniaod"
  ps = "aod"
  cl = "AOD"

if args.gen:

  wanted_events = 200000
  if not args.run_all:
    if "matched_xqcut_up" in args.tarball:
      nevents = wanted_events*1.25
      cfg = "run_gen_matched_up_{}.py".format(args.year)
    elif "matched_xqcut_down" in args.tarball:
      nevents = wanted_events*2.5
      cfg = "run_gen_matched_down_{}.py".format(args.year)
    elif "matched" in args.tarball:
      nevents = wanted_events*1.6
      cfg = "run_gen_matched_{}.py".format(args.year)
    else:
      nevents = wanted_events
      cfg = "gen_{}_cfg.py".format(args.year)

    ReadReplaceAndWrite("analysis_chain/templates/run_gen_matched_{}.py".format(args.year),"{}_{}_{}.py".format(mn,args.folder_name,args.year),args.tarball,args.folder_name)  
    ReadReplaceAndWrite("analysis_chain/templates/crab_{}_{}.py".format(mn,args.year),"crab_{}_{}.py".format(mn,args.folder_name),args.tarball,args.folder_name)
    if not args.dry_run: os.system("crab submit crab_{}_{}.py".format(mn,args.folder_name))
  else:
    for tarball in os.listdir("./"):
      if "tar.xz" in tarball and args.skip != tarball:
        if "matched_xqcut_up" in tarball:
          nevents = wanted_events*1.25
          cfg = "run_gen_matched_up_{}.py".format(args.year)
        elif "matched_xqcut_down" in tarball:
          nevents = wanted_events*2.5
          cfg = "run_gen_matched_down_{}.py".format(args.year)
        elif "matched" in tarball:
          nevents = wanted_events*1.6
          cfg = "run_gen_matched_{}.py".format(args.year)
        else:
          nevents = wanted_events
          cfg = "gen_{}_cfg.py".format(args.year)
        folder_name = tarball.replace("_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz","")
        ReadReplaceAndWrite("analysis_chain/templates/{}".format(cfg),"{}_{}_{}.py".format(mn,folder_name,args.year),tarball,folder_name,nevents=int(nevents))
        ReadReplaceAndWrite("analysis_chain/templates/crab_{}_{}.py".format(mn,args.year),"crab_{}_{}.py".format(mn,folder_name),tarball,folder_name,nevents=int(nevents))
        if not args.dry_run: os.system("crab submit crab_{}_{}.py".format(mn,folder_name))
else:
  if not args.run_all: it_over = [args.folder_name]
  else:  
    it_over = []
    for tarball in os.listdir("./"):
      if "tar.xz" in tarball and args.skip != tarball:
        it_over.append(tarball.replace("_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz",""))
  tasks_to_add = []
  for i in it_over:
    tasks_to_add.append("tasks.append(('{}_{}_{}', '{}', '{}_{}_{}'))".format(i,args.year,mn.upper(),get_dataset(i,ps,cl),i,args.year,mn.upper()))
 
  ReadReplaceAndWrite("analysis_chain/templates/{}_{}_cfg.py".format(mn,args.year),"{}_{}.py".format(mn,args.year),"","")
  ReadReplaceAndWrite("analysis_chain/templates/crab_{}.py".format(mn),"crab_{}.py".format(mn),"","",add_tasks=True,lines_to_add=tasks_to_add)
  if not args.dry_run: os.system("python crab_{}.py".format(mn))
 

