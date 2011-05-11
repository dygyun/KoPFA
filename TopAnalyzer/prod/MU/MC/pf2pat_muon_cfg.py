import FWCore.ParameterSet.Config as cms

from KoPFA.TopAnalyzer.pf2pat_template_cfg import *

postfix = "PFlow"
jetAlgo="AK5"
usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=True, postfix=postfix)

updateEventContent(process)

#REMOVE ISOLATION FROM PF2PAT!!!
process.pfIsolatedMuonsPFlow.combinedIsolationCut = cms.double(999)
process.pfIsolatedElectronsPFlow.combinedIsolationCut = cms.double(999)

process.patMuonFilter.minNumber = 2

## Source
#process.source = cms.Source("PoolSource",
#                                fileNames = cms.untracked.vstring(
#  '/store/data/Run2011A/DoubleMu/RECO/PromptReco-v1/000/161/312/9CD2FBA7-E557-E011-B433-001D09F29849.root'
#  )
#)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#process.p += process.hltHighLevelMuMuMC 
process.p += getattr(process,"patPF2PATSequence"+postfix)
process.p += process.acceptedMuons
process.p += process.patMuonFilter

# top projections in PF2PAT:
getattr(process,"pfNoPileUp"+postfix).enable = True
getattr(process,"pfNoMuon"+postfix).enable = True
getattr(process,"pfNoElectron"+postfix).enable = True
getattr(process,"pfNoTau"+postfix).enable = False # to use tau-cleaned jet collection : True
getattr(process,"pfNoJet"+postfix).enable = True

process.MessageLogger.cerr.FwkReport.reportEvery = 100

