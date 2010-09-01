
import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
		     noEventSort = cms.untracked.bool(True),
		     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
		     fileNames = readFiles
                    )
readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_10_0_7NO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_11_0_1n4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_12_0_rlN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_13_0_oYZ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_14_0_8ej.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_15_0_JSR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_16_0_Xho.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_17_0_hEG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_18_1_LAu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_19_0_cRj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_1_1_Zdd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_20_1_4bF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_21_0_ATc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_22_1_bMQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_23_0_JOw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_24_0_POb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_25_0_zSF.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_26_0_xDs.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_27_0_Xht.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_28_0_mzX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_29_0_fCJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_2_0_KTx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_30_0_42O.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_31_0_iG6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_32_0_JOP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_33_0_rKx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_34_0_wzH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_35_0_bKf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_36_0_GE2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_37_0_BNC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_38_0_BDT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_39_0_N4l.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_3_0_pU6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_40_0_Q3o.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_41_1_9df.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_42_0_3ym.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_43_0_cpd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_44_0_HrN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_45_1_85v.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_46_1_Aby.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_47_0_ry2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_48_0_nuw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_49_0_EEk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_4_0_y81.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_50_0_YrK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_51_0_P27.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_52_0_w5l.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_53_0_W6C.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_54_0_YzI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_55_0_840.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_56_0_4ah.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_57_0_uUQ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_58_0_wnE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_59_0_PcR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_5_0_QSx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_60_0_f8Z.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_61_0_f2Q.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_62_0_YYy.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_63_0_Wrj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_64_1_4Dj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_65_1_fGD.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_6_1_W89.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_7_0_y4i.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_8_0_HXX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/MUSKIM/Aug13_nopileup/Commissioning10-SD_Mu-Jun14thSkim_v1/patTuple_muon_9_0_Omo.root',
]
        )
