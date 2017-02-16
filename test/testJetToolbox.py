import FWCore.ParameterSet.Config as cms

process = cms.Process('jetToolbox')

process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_v4'

process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.suppressWarning = cms.untracked.vstring('ecalLaserCorrFilter','manystripclus53X','toomanystripclus53X')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)

from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox

listBTagInfos = ['pfInclusiveSecondaryVertexFinderTagInfos'] 
listBtagDiscriminatorsAK8 = [
	'pfCombinedInclusiveSecondaryVertexV2BJetTags',
	'pfBoostedDoubleSecondaryVertexAK8BJetTags'
]
jetToolbox(process,
	'ak8',
	'jetSequence',
	'out',
	PUMethod = 'Puppi',
	miniAOD = True,
	runOnMC = True,
	Cut = 'pt>170.',
	addSoftDrop = True,
	addSoftDropSubjets = True,
	addNsub = True,
	bTagInfos = listBTagInfos, 
	bTagDiscriminators = listBtagDiscriminatorsAK8, 
	maxTau = 3,
)

jetToolbox(process,
	'ak8',
	'jetSequence',
	'out',
	PUMethod = 'newPuppi',
	postFix = 'new',
	miniAOD = True,
	runOnMC = True,
	Cut = 'pt>170.',
	addSoftDrop = True,
	addSoftDropSubjets = True,
	addNsub = True,
	bTagInfos = listBTagInfos, 
	bTagDiscriminators = listBtagDiscriminatorsAK8, 
	maxTau = 3,
)
process.out.outputCommands.extend([
    'keep patPackedCandidates_*_*_*',
#    'keep *Association*_*_*_*',
])

process.endpath = cms.EndPath(process.out)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
	    #'file:store_mc_RunIISummer16MiniAODv2_GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_MINIAODSIM_PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_120000_0010CF3F-1EB7-E611-A46F-00266CFFA678.root'
	    '/store/mc/RunIISummer16MiniAODv2/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/BA6C4FC3-8FBC-E611-85B6-0CC47A4D7662.root',
	    '/store/mc/RunIISummer16MiniAODv2/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/E2386F98-8DBC-E611-9832-0025905A60FE.root',
	    '/store/mc/RunIISummer16MiniAODv2/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/DAE8BC48-92BC-E611-916A-0CC47A78A4A0.root',
	    '/store/mc/RunIISummer16MiniAODv2/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/46FF811A-A1BC-E611-82E7-0CC47A4C8F18.root',
	    )
)

#from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValTTbarPileUpMINIAODSIM
#process.source.fileNames = filesRelValTTbarPileUpMINIAODSIM
