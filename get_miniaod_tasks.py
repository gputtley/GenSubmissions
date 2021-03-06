import os 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--year',help= 'Year for config to run with', default='2018')
args = parser.parse_args()

def get_dataset(folder):
  os.system("crab status MINIAOD/crab_%(folder)s >> crab_status_output.txt" % vars())
  crab_status_file = open('crab_status_output.txt', 'r')
  for line in crab_status_file:
    if "Output dataset:" in line:
      output_dataset = line.split("Output dataset:")[1].strip()
  os.system("rm crab_status_output.txt")
  return output_dataset

tasks_to_add = []
for i in os.listdir("MINIAOD/"):
  name = i.replace("crab_","")
  tasks_to_add.append("tasks.append(('VectorLQToTauTau_{}', '{}'))".format(name.replace("_{}_MINIAOD".format(args.year),""),get_dataset(name)))

for i in tasks_to_add: print i
