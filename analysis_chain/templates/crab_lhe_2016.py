from CRABClient.UserUtilities import config
config = config()

config.General.requestName     = 'bbh_m200_2016_LHE'
config.General.workArea        = 'bbh_m200_2016_LHE'
config.General.transferOutputs = True
config.General.transferLogs    = True
#config.JobType.numCores = 4
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'lhe_2016.py'

config.JobType.allowUndistributedCMSSW = True
config.Data.outputPrimaryDataset = 'bbh_m200_LHE'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 200000
config.Data.totalUnits           = 1000000
config.Data.outLFNDirBase        = '/store/user/dwinterb/bbh_m200_LHE/'
config.Data.publication          = True
config.Data.outputDatasetTag     = 'bbh_m200_2016_LHE'
config.JobType.inputFiles = ['bbh_powheg_m200.tar.gz']


config.Site.storageSite = 'T2_UK_London_IC'
