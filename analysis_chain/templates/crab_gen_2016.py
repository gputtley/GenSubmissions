from CRABClient.UserUtilities import config
from multiprocessing import Process
config = config()

config.General.requestName     = 'GEN'
config.General.workArea        = 'GEN'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'gen_from_lhe_2016.py'

config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 500
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/dwinterb/bbH_GEN/'
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

    tasks.append(('bbH_m200_2016_GEN', 'copy_dataset_name_here', 'bbH_m200_2016_GEN'))

    for task in tasks:
        print task[0]
        config.Data.outputDatasetTag = task[2]
        config.General.requestName = task[2]
        config.Data.inputDataset = task[1]
        #submit(config)

        p = Process(target=submit, args=(config,))
        p.start()
        p.join()



