from CRABClient.UserUtilities import config
from multiprocessing import Process
config = config()

config.General.requestName     = 'RECO'
config.General.workArea        = 'RECO'
config.General.transferOutputs = True
config.General.transferLogs    = True
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 15000

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'RECO_YEAR_NAME_cfg.py'

config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 1000
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/USER_NAME/RECO/'
config.Data.publication          = True
config.Data.ignoreLocality      = True

config.Site.whitelist   = ['T2_*','T1_*','T3_*']
config.Site.storageSite = 'T2_UK_London_IC'


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print hte.headers

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    tasks=list()

    for task in tasks:
        print task[0]
        config.Data.outputDatasetTag = task[2]
        config.General.requestName = task[2]
        config.Data.inputDataset = task[1]
        #submit(config)

        p = Process(target=submit, args=(config,))
        p.start()
        p.join()



