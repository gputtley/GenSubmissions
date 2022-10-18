import os 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--year',help= 'Year for config to run with', default='2018')
args = parser.parse_args()

def get_dataset(folder,cmssw):
  os.system("crab status %(cmssw)s/src/MiniAOD/crab_%(folder)s >> crab_status_output.txt" % vars())
  crab_status_file = open('crab_status_output.txt', 'r')
  for line in crab_status_file:
    if "Output dataset:" in line:
      output_dataset = line.split("Output dataset:")[1].strip()
  os.system("rm crab_status_output.txt")
  return output_dataset

f = open("templates/cmssw_to_use_{}.txt".format(args.year), "r")
for ind,x in enumerate(f):
  if x.split(" ")[0] == "MiniAOD": cmssw = x.split(" ")[1].rstrip()

tasks_to_add = []
for i in os.listdir("%(cmssw)s/src/MiniAOD/" % vars()):
  name = i.replace("crab_","")
  tasks_to_add.append("tasks.append(('{}', '{}'))".format(name.replace("_{}_MiniAOD".format(args.year),""),get_dataset(name,cmssw)))

for i in tasks_to_add: print i
