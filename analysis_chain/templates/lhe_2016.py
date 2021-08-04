# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename lhe_2016.py --eventcontent LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier LHE --fileout file:LHE.root --conditions MCRUN2_71_V1::All --step NONE --filein root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/pwgevents-0011.lhe --no_exec --mc -n 20
import FWCore.ParameterSet.Config as cms

process = cms.Process('LHE')

# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0103.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0001.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0002.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0003.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0004.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0005.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0006.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0008.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0009.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0011.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0012.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0013.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0014.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0015.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0016.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0017.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0018.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0019.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0020.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0021.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0022.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0027.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0028.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0029.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0030.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0031.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0032.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0033.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0034.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0035.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0044.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0047.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0050.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0051.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0053.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0054.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0055.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0057.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0058.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0061.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0065.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0066.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0067.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0069.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0071.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0074.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0085.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0086.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0087.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0088.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0089.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0090.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0092.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0093.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0095.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0096.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0097.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0098.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0099.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0100.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0101.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0102.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0104.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0105.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0106.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0107.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0108.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0109.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0114.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0115.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0116.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0117.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0118.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0119.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0120.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0121.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0122.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0123.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0124.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0125.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0126.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0127.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0128.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0129.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0130.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0131.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0132.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0133.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0134.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0135.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0136.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0137.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0138.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0139.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0140.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0141.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0142.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0143.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0144.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0146.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0149.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0151.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0156.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0157.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0162.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0163.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0164.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0165.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0166.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0167.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0168.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0169.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0170.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0171.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0172.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0173.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0174.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0175.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0176.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0177.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0178.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0179.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0180.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0181.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0182.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0183.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0184.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0185.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0186.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0187.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0188.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0189.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0190.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0191.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0192.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0193.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0194.lhe',
'root://gfe02.grid.hep.ph.ic.ac.uk:1097/store/user/dwinterb/bbh_m200_2016_lhe/cmsgrid_final_pwgevents-0195.lhe')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('--python_filename nevts:20'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.LHEEventContent.outputCommands,
    fileName = cms.untracked.string('file:LHE.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('LHE')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

# Path and EndPath definitions
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.LHEoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
