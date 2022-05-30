from CRABClient.UserUtilities import config

config = config()

config.General.requestName     = 'SAMPLE_FILENAME'
config.General.workArea        = 'SAMPLE_FILENAME'
config.General.transferOutputs = True
config.General.transferLogs    = True
#config.JobType.numCores = 4
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'LHEGEN_SAMPLE_FILENAME_2018.py'

config.JobType.allowUndistributedCMSSW = True
config.Data.outputPrimaryDataset = 'SAMPLE_FILENAME'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 500
config.Data.totalUnits           = N_EVENTS
config.Data.outLFNDirBase        = '/store/user/guttley/DCACHE_FOLDER/SAMPLE_FILENAME_LHEGEN_2018/'
config.Data.publication          = True
config.Data.outputDatasetTag     = 'SAMPLE_FILENAME'
config.JobType.inputFiles = ['TARBALL_FILENAME']


config.Site.storageSite = 'T2_UK_London_IC'

