# python run_gridpacks.py --input="/afs/cern.ch/work/g/guttley/private/genproductions_fork/genproductions/bin/MadGraph5_aMCatNLO/4tau_GenSubmissions/gridpacks/" --year=2018 --run_all --dry_run

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input',help= 'location of input gridpacks', default='gridpacks/')
parser.add_argument('--year',help= 'Year for config to run with', default='2018')
parser.add_argument('--tarball',help= 'Inset name of tarball, only need for --gen', default='')
parser.add_argument("--dry_run", action='store_true',help="Will create files but not run them")
parser.add_argument("--run_all", action='store_true',help="Will run all tar.xz files in input directory")
parser.add_argument('--skip',help= 'If running with --run_all will skip this tarball', default='')
parser.add_argument('--events',help= 'Number of events to run for', default='200000')
parser.add_argument('--username',help= 'CERN username', default='guttley')
args = parser.parse_args()

f = open("templates/cmssw_to_use_{}.txt".format(args.year), "r")
steps = []
cmssws = []
for ind,x in enumerate(f):
  if x.count(" 1") == 1: step = ind
  cmssws.append(x.split(" ")[1].rstrip())
  steps.append(x.split(" ")[0])

nevents = args.events
CMSSW = cmssws[step]


def ReadReplaceAndWrite(template,filename,tarball_name,folder_name,year,username,add_tasks=False,lines_to_add=[],nevents=None):
  # Read in the file
  with open(template, 'r') as file :
    filedata = file.read()
  
  # Replace the target string
  filedata = filedata.replace('TARBALL_FILENAME',tarball_name).replace('SAMPLE_FILENAME',folder_name).replace("YEAR_NAME",year).replace("USER_NAME",username)

  if nevents != None: filedata = filedata.replace("NEVENTS",str(nevents))

  if add_tasks:
    add_lines='tasks=list()\n'
    for i in lines_to_add:
      add_lines += "    "+i+"\n"
    filedata = filedata.replace("tasks=list()",add_lines)

  # Write the file out again
  with open(filename, 'w') as file:
    file.write(filedata)

def get_dataset(folder,steps,cmssws,step):
  ps = steps[step-1]
  pCMSSW = cmssws[step-1]
  year = args.year
  if step == 1:
    os.system("crab status %(pCMSSW)s/src/%(folder)s/crab_%(folder)s >> crab_status_output.txt" % vars())
  else:
      print "crab status %(pCMSSW)s/src/%(ps)s/crab_%(folder)s_%(year)s_%(ps)s >> crab_status_output.txt" % vars()
      os.system("crab status %(pCMSSW)s/src/%(ps)s/crab_%(folder)s_%(year)s_%(ps)s >> crab_status_output.txt" % vars())
  crab_status_file = open('crab_status_output.txt', 'r')
  for line in crab_status_file:
    if "Output dataset:" in line:
      output_dataset = line.split("Output dataset:")[1].strip()
  os.system("rm crab_status_output.txt")
  return output_dataset

def WriteListToFile(lst,output_name):
  textfile = open(output_name, "w")
  for i in lst:
    textfile.write(i + "\n")
  textfile.close()

tarball_ext = "_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz"

if step == 0:
    for tarball in os.listdir(args.input):
      if "tar.xz" in tarball and tarball not in args.skip.split(","):
        folder_name = tarball.replace(tarball_ext,"")
        if args.run_all or (args.tarball == tarball):
          cfg = "{}_{}_cfg.py".format(steps[step],args.year)
          new_cfg = "{}_{}_{}.py".format(steps[step],folder_name,args.year)
          sub = "crab_{}.py".format(steps[step])
          new_sub = "crab_{}_{}_{}.py".format(steps[step],folder_name,args.year)
          ReadReplaceAndWrite("templates/{}".format(cfg),new_cfg,tarball,folder_name,args.year,args.username,nevents=int(nevents))  
          ReadReplaceAndWrite("templates/{}".format(sub),new_sub,tarball,folder_name,args.year,args.username,nevents=int(nevents))
          setup_file = ["source /cvmfs/cms.cern.ch/cmsset_default.sh",
                      "if [ -r {} ] ; then".format(CMSSW),
                      "  echo release {} already exists".format(CMSSW),
                      "else",
                      "  scram p CMSSW {}".format(CMSSW),
                      "fi",
                      "mv {} {}/src/".format(new_cfg,CMSSW),
                      "mv {} {}/src/".format(new_sub,CMSSW),
                      "cp {}/{} {}/src/".format(args.input,tarball,CMSSW)]
          run_file = ["cd {}/src".format(CMSSW),
                      "eval `scram runtime -sh`"]
          if not args.dry_run: run_file.append("crab submit {}".format(new_sub))
          WriteListToFile(setup_file,"setup_file_{}_{}_{}.sh".format(steps[step],folder_name,args.year))
          WriteListToFile(run_file,"run_file_{}_{}_{}.sh".format(steps[step],folder_name,args.year))
          os.system("bash setup_file_{}_{}_{}.sh".format(steps[step],folder_name,args.year))
          os.system("rm setup_file_{}_{}_{}.sh".format(steps[step],folder_name,args.year))
          os.system("bash run_file_{}_{}_{}.sh".format(steps[step],folder_name,args.year))
          os.system("rm run_file_{}_{}_{}.sh".format(steps[step],folder_name,args.year))
else:
  if not args.run_all: it_over = [args.folder_name]
  else:  
    it_over = []
    for tarball in os.listdir(args.input):
      if "tar.xz" in tarball and tarball not in args.skip.split(","):
        it_over.append(tarball.replace(tarball_ext,""))
  tasks_to_add = []
  for i in it_over:
    tasks_to_add.append("tasks.append(('{}_{}_{}', '{}', '{}_{}_{}'))".format(i,args.year,steps[step],get_dataset(i,steps,cmssws,step),i,args.year,steps[step]))
 
  new_cfg = "{}_{}_cfg.py".format(steps[step],args.year)
  new_sub = "crab_{}_{}.py".format(steps[step],args.year)
  ReadReplaceAndWrite("templates/{}_{}_cfg.py".format(steps[step],args.year),new_cfg,"","",args.year.args.username)
  ReadReplaceAndWrite("templates/crab_{}.py".format(steps[step]),new_sub,"","",args.year,args.username,add_tasks=True,lines_to_add=tasks_to_add)
  setup_file = ["source /cvmfs/cms.cern.ch/cmsset_default.sh",
              "if [ -r {} ] ; then".format(CMSSW),
              "  echo release {} already exists".format(CMSSW),
              "else",
              "  scram p CMSSW {}".format(CMSSW),
              "fi",
              "mv {} {}/src/".format(new_cfg,CMSSW),
              "mv {} {}/src/".format(new_sub,CMSSW)]
  run_file = ["cd {}/src".format(CMSSW),
              "eval `scram runtime -sh`"]

  if not args.dry_run: run_file.append("python crab_{}_{}.py".format(steps[step],args.year))
  WriteListToFile(setup_file,"setup_file_{}_{}.sh".format(steps[step],args.year))
  WriteListToFile(run_file,"run_file_{}_{}.sh".format(steps[step],args.year))
  os.system("bash setup_file_{}_{}.sh".format(steps[step],args.year))
  os.system("rm setup_file_{}_{}.sh".format(steps[step],args.year))
  os.system("bash run_file_{}_{}.sh".format(steps[step],args.year))
  os.system("rm run_file_{}_{}.sh".format(steps[step],args.year))

 
if not args.dry_run:
  new_cmssw_to_use = []
  for ind, val in enumerate(steps):
    if step == ind - 1:
      new_cmssw_to_use.append(val + " " + cmssws[ind] + " 1")
    else:
      new_cmssw_to_use.append(val + " " + cmssws[ind])
  WriteListToFile(new_cmssw_to_use,"templates/cmssw_to_use_{}.txt".format(args.year))

