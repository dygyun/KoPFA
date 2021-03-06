
import FWCore.ParameterSet.Config as cms

source = cms.Source(
	"PoolSource",
	noEventSort = cms.untracked.bool(True),
	duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
	fileNames = cms.untracked.vstring()
)
source.fileNames.extend([
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_1.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_10.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_100.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_101.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_102.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_103.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_104.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_105.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_106.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_107.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_108.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_109.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_11.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_110.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_111.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_112.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_113.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_114.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_115.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_116.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_117.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_118.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_119.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_12.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_120.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_121.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_122.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_123.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_124.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_125.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_126.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_127.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_128.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_129.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_13.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_130.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_131.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_132.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_133.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_134.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_135.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_136.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_137.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_138.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_139.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_14.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_140.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_141.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_142.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_143.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_144.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_145.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_146.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_147.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_148.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_149.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_15.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_150.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_151.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_152.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_153.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_154.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_155.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_156.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_157.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_158.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_159.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_16.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_160.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_161.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_162.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_163.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_164.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_165.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_166.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_167.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_168.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_169.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_17.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_170.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_171.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_172.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_173.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_174.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_175.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_176.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_177.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_178.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_179.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_18.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_180.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_181.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_182.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_183.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_184.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_185.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_186.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_187.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_188.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_189.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_19.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_190.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_191.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_192.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_193.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_194.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_195.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_196.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_197.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_198.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_199.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_2.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_20.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_200.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_201.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_202.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_203.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_204.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_205.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_206.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_207.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_208.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_209.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_21.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_210.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_211.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_212.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_213.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_214.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_215.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_216.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_217.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_218.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_219.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_22.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_220.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_221.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_222.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_223.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_224.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_225.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_226.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_227.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_228.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_229.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_23.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_230.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_231.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_232.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_233.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_234.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_235.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_236.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_237.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_238.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_239.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_24.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_240.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_241.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_242.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_243.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_244.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_245.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_246.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_247.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_248.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_249.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_25.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_250.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_251.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_252.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_253.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_254.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_255.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_256.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_257.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_258.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_26.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_27.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_28.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_29.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_3.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_30.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_31.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_32.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_33.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_34.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_35.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_36.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_37.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_38.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_39.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_4.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_40.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_41.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_42.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_43.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_44.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_45.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_46.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_47.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_48.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_49.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_5.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_50.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_51.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_52.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_53.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_54.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_55.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_56.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_57.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_58.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_59.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_6.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_60.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_61.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_62.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_63.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_64.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_65.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_66.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_67.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_68.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_69.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_7.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_70.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_71.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_72.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_73.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_74.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_75.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_76.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_77.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_78.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_79.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_8.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_80.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_81.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_82.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_83.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_84.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_85.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_86.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_87.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_88.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_89.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_9.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_90.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_91.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_92.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_93.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_94.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_95.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_96.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_97.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_98.root',
		'/store/cmst3/user/cmgtools/CMG/MuEG/Run2011A-05Aug2011-v1/AOD/PAT_CMG_V5_12_0_44X/cmgTuple_99.root',
])
