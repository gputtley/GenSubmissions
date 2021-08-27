from CRABClient.UserUtilities import config
config = config()

config.General.requestName     = 'SAMPLE_FILENAME_LHE'
config.General.workArea        = 'SAMPLE_FILENAME_LHE'
config.General.transferOutputs = True
config.General.transferLogs    = True
#config.JobType.numCores = 4
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'SAMPLE_FILENAME_lhe_2016.py'

config.JobType.allowUndistributedCMSSW = True
config.Data.outputPrimaryDataset = 'SAMPLE_FILENAME_LHE'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 100000
config.Data.totalUnits           = 1000000
config.Data.outLFNDirBase        = '/store/user/guttley/SAMPLE_FILENAME_LHE/'
config.Data.publication          = True
config.Data.outputDatasetTag     = 'SAMPLE_FILENAME_LHE'
config.JobType.inputFiles = ['TARBALL_FILENAME']


config.Site.storageSite = 'T2_UK_London_IC'
