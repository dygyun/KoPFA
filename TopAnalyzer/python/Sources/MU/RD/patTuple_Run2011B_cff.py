
import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
		     noEventSort = cms.untracked.bool(True),
		     duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
		     fileNames = readFiles
                    )
readFiles.extend([
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_100_0_rEU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_101_0_cvb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_102_0_fi8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_103_0_jN0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_104_0_Y8h.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_105_0_Gcf.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_106_0_8C8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_107_0_zGE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_108_1_b5o.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_109_0_um2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_10_1_q9H.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_110_0_pZ7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_111_0_gpG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_112_0_jxC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_113_0_JWd.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_114_0_7he.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_115_0_2pl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_116_0_xbU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_117_0_VcI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_118_0_QDi.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_119_0_H9F.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_11_1_vKC.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_120_0_scG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_121_0_gBm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_122_0_TeJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_123_1_qGB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_124_0_ScJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_125_0_NIh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_126_0_FGG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_127_1_w7i.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_128_0_SeO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_129_0_gxH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_12_1_PMr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_130_0_9MN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_131_0_iU8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_132_1_p0W.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_133_0_hfN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_134_0_FEP.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_135_1_O2v.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_136_0_Jig.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_137_1_CRV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_138_0_TXb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_139_0_q56.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_13_1_ROw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_140_0_aXR.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_141_0_eXz.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_142_0_jmO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_143_0_KCi.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_144_0_Lci.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_145_1_ZRY.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_146_0_16t.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_147_0_PYS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_148_0_2t3.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_149_0_dRV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_14_1_d7v.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_150_0_AkO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_151_1_GCv.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_152_0_DHB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_153_0_kut.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_154_0_CWt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_155_0_1BS.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_156_0_lGc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_15_1_v7n.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_16_3_Bgu.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_17_1_Kq6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_18_1_6ZT.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_19_1_Tpm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_1_1_TBN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_20_1_XIE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_21_1_2Fh.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_22_1_jgL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_23_1_ovM.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_24_2_joG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_25_2_qzL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_26_1_Cr7.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_27_0_3aI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_28_0_GzH.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_29_0_Wam.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_2_1_Y0R.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_30_0_rU6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_31_0_a4t.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_32_0_g4w.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_33_0_nRg.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_34_1_JLm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_35_0_Zaj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_36_1_cf2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_37_0_heJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_38_1_rGU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_39_0_mq6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_3_1_ibo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_40_1_P1O.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_41_0_jEl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_42_0_wus.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_43_1_okp.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_44_0_D28.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_45_0_ayo.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_46_1_y6W.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_47_0_Jok.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_48_0_pp8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_49_1_5vc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_4_1_6Sk.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_50_0_J2N.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_51_0_Amr.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_52_0_s0x.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_53_0_tXV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_54_2_WHb.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_55_1_hN6.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_56_0_9Z2.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_57_0_gwG.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_58_0_95x.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_59_0_EMl.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_5_1_ZaE.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_60_0_Hut.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_61_0_uyN.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_62_0_3rn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_63_0_o5R.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_64_0_TXc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_65_0_Br0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_66_0_d7z.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_67_0_eDa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_68_0_66o.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_69_0_9HJ.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_6_1_ZtI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_70_1_5Nm.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_71_0_HE0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_72_0_w5v.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_73_0_a3Z.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_74_0_sUx.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_75_0_NIV.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_76_0_Uoj.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_77_0_9vO.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_78_0_Ibt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_79_0_bGn.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_7_3_M2e.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_80_0_RIX.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_81_0_8aL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_82_0_bow.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_83_0_N5V.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_84_0_ELw.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_85_0_NWt.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_86_0_o9R.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_87_0_hrK.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_88_0_QH8.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_89_1_Ixc.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_8_1_Bv0.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_90_0_rf4.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_91_0_5YL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_92_0_lTi.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_93_1_n6p.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_94_0_877.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_95_0_hJI.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_96_0_AiB.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_97_0_3YL.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_98_1_hSU.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_99_0_wqa.root',
	'rfio:///castor/cern.ch/user/t/tjkim/2011data/DoubleMu/Dec19/Run2011B-PromptReco-v1/patTuple_skim_9_1_5uy.root',
]
        )
