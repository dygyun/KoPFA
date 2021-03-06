from KoPFA.IsoAnalyzer.MuonIsoAna_cff import process

import FWCore.ParameterSet.Config as cms

process.load("KoPFA.DiMuonAnalyzer.MC.Fall10_Single_MUSKIM.patTuple_TTbar_TightMU_cff")

process.hltHighLevel.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
