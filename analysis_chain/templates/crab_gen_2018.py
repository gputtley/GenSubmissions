from CRABClient.UserUtilities import config

config = config()

config.General.requestName     = 'SAMPLE_FILENAME_GENSIM_2018'
config.General.workArea        = 'SAMPLE_FILENAME_GENSIM_2018'
config.General.transferOutputs = True
config.General.transferLogs    = True
#config.JobType.numCores = 4
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'gen_SAMPLE_FILENAME_2018.py'

config.JobType.allowUndistributedCMSSW = True
config.Data.outputPrimaryDataset = 'SAMPLE_FILENAME_GENSIM_2018'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 500
config.Data.totalUnits           = 200000
config.Data.outLFNDirBase        = '/store/user/guttley/SAMPLE_FILENAME_GENSIM_2018/'
config.Data.publication          = True
config.Data.outputDatasetTag     = 'SAMPLE_FILENAME_GENSIM_2018'
config.JobType.inputFiles = ['TARBALL_FILENAME']


config.Site.storageSite = 'T2_UK_London_IC'

