from CRABClient.UserUtilities import config
config = config()

config.General.requestName     = 'betaRd33_0_mU1000_gU1_LHE'
config.General.workArea        = 'betaRd33_0_mU1000_gU1_LHE'
config.General.transferOutputs = True
config.General.transferLogs    = True
#config.JobType.numCores = 4
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'lhe_2016.py'

config.JobType.allowUndistributedCMSSW = True
config.Data.outputPrimaryDataset = 'betaRd33_0_mU1000_gU1_LHE'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 200000
config.Data.totalUnits           = 1000000
config.Data.outLFNDirBase        = '/store/user/guttley/betaRd33_0_mU1000_gU1_LHE/'
config.Data.publication          = True
config.Data.outputDatasetTag     = 'betaRd33_0_mU1000_gU1_LHE'
config.JobType.inputFiles = ['betaRd33_0_mU1000_gU1_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz']


config.Site.storageSite = 'T2_UK_London_IC'
