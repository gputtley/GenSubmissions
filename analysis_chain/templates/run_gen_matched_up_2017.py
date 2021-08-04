# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/MUO-RunIIFall17wmLHEGS-00004-fragment.py --python_filename run_gen_matched_2017.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --fileout file:output.root --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int(1)\nprocess.source.numberEventsInLuminosityBlock=cms.untracked.uint32(227) --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2017 --no_exec --mc -n 200
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/MUO-RunIIFall17wmLHEGS-00004-fragment.py nevts:20'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:output.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('LHE'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:output_inLHE.root'),
    outputCommands = process.LHEEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '93X_mc2017_realistic_v3', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'pythia8PSweightsSettings', 
            'processParameters'),
        processParameters = cms.vstring('JetMatching:setMad = off', 
            'JetMatching:scheme = 1', 
            'JetMatching:merge = on', 
            'JetMatching:jetAlgorithm = 2', 
            'JetMatching:etaJetMax = 5.', 
            'JetMatching:coneRadius = 1.', 
            'JetMatching:slowJetPower = 1', 
            'JetMatching:qCut = 80.', 
            'JetMatching:nQmatch = 5', 
            'JetMatching:nJetMax = 1', 
            'JetMatching:doShowerKt = off', 
            'TimeShower:mMaxGamma = 4.0'),
        pythia8CP5Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'PDF:pSet=20', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118'),
        pythia8PSweightsSettings = cms.vstring(
            'UncertaintyBands:doVariations = on',
    # 3 sets of variations for ISR&FSR up/down
    # Reduced sqrt(2)/(1/sqrt(2)), Default 2/0.5 and Conservative 4/0.25 variations
    # 32 decorrelated variations of muR and non-singular terms (cNS) for each branching type
            'UncertaintyBands:List = {\
    isrRedHi isr:muRfac=0.707,fsrRedHi fsr:muRfac=0.707,isrRedLo isr:muRfac=1.414,fsrRedLo fsr:muRfac=1.414,\
    isrDefHi isr:muRfac=0.5,fsrDefHi fsr:muRfac=0.5,isrDefLo isr:muRfac=2.0,fsrDefLo fsr:muRfac=2.0,\
    isrConHi isr:muRfac=0.25,fsrConHi fsr:muRfac=0.25,isrConLo isr:muRfac=4.0,fsrConLo fsr:muRfac=4.0,\
    fsr_G2GG_muR_dn fsr:G2GG:muRfac=0.5,\
    fsr_G2GG_muR_up fsr:G2GG:muRfac=2.0,\
    fsr_G2QQ_muR_dn fsr:G2QQ:muRfac=0.5,\
    fsr_G2QQ_muR_up fsr:G2QQ:muRfac=2.0,\
    fsr_Q2QG_muR_dn fsr:Q2QG:muRfac=0.5,\
    fsr_Q2QG_muR_up fsr:Q2QG:muRfac=2.0,\
    fsr_X2XG_muR_dn fsr:X2XG:muRfac=0.5,\
    fsr_X2XG_muR_up fsr:X2XG:muRfac=2.0,\
    fsr_G2GG_cNS_dn fsr:G2GG:cNS=-2.0,\
    fsr_G2GG_cNS_up fsr:G2GG:cNS=2.0,\
    fsr_G2QQ_cNS_dn fsr:G2QQ:cNS=-2.0,\
    fsr_G2QQ_cNS_up fsr:G2QQ:cNS=2.0,\
    fsr_Q2QG_cNS_dn fsr:Q2QG:cNS=-2.0,\
    fsr_Q2QG_cNS_up fsr:Q2QG:cNS=2.0,\
    fsr_X2XG_cNS_dn fsr:X2XG:cNS=-2.0,\
    fsr_X2XG_cNS_up fsr:X2XG:cNS=2.0,\
    isr_G2GG_muR_dn isr:G2GG:muRfac=0.5,\
    isr_G2GG_muR_up isr:G2GG:muRfac=2.0,\
    isr_G2QQ_muR_dn isr:G2QQ:muRfac=0.5,\
    isr_G2QQ_muR_up isr:G2QQ:muRfac=2.0,\
    isr_Q2QG_muR_dn isr:Q2QG:muRfac=0.5,\
    isr_Q2QG_muR_up isr:Q2QG:muRfac=2.0,\
    isr_X2XG_muR_dn isr:X2XG:muRfac=0.5,\
    isr_X2XG_muR_up isr:X2XG:muRfac=2.0,\
    isr_G2GG_cNS_dn isr:G2GG:cNS=-2.0,\
    isr_G2GG_cNS_up isr:G2GG:cNS=2.0,\
    isr_G2QQ_cNS_dn isr:G2QQ:cNS=-2.0,\
    isr_G2QQ_cNS_up isr:G2QQ:cNS=2.0,\
    isr_Q2QG_cNS_dn isr:Q2QG:cNS=-2.0,\
    isr_Q2QG_cNS_up isr:Q2QG:cNS=2.0,\
    isr_X2XG_cNS_dn isr:X2XG:cNS=-2.0,\
    isr_X2XG_cNS_up isr:X2XG:cNS=2.0}',

            'UncertaintyBands:nFlavQ = 4', # define X=bottom/top in X2XG variations
            'UncertaintyBands:MPIshowers = on',
            'UncertaintyBands:overSampleFSR = 10.0',
            'UncertaintyBands:overSampleISR = 10.0',
            'UncertaintyBands:FSRpTmin2Fac = 20',
            'UncertaintyBands:ISRpTmin2Fac = 1'
        ),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/afs/cern.ch/work/d/dwinterb/private/lqmc/genproductions/bin/MadGraph5_aMCatNLO/betaRd33_0_mU4_gU1_matched_xqcut_up_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(20),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int(1)
process.source.numberEventsInLuminosityBlock=cms.untracked.uint32(227)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
