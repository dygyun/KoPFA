#include "KoPFA/IsoAnalyzer/interface/cmgMuonIsoAnalyzer.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/Common/interface/Ptr.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "TLorentzVector.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

using namespace std;

cmgMuonIsoAnalyzer::cmgMuonIsoAnalyzer(const edm::ParameterSet& config)
{
  muonLabel_ = config.getParameter<edm::InputTag>("muonLabel");
  beamSpotLabel_ = config.getParameter<edm::InputTag>("beamSpotLabel");
  //metLabel_ = config.getParameter<edm::InputTag>("metLabel");
  //jetLabel_ = config.getParameter<edm::InputTag>("jetLabel");
  metLabel_ = config.getParameter<edm::InputTag>("metLabel");
  jetLabel_ = config.getParameter<edm::InputTag>("jetLabel");
  genParticlesLabel_= config.getParameter<edm::InputTag>("genParticlesLabel");
  vertexLabel_ =  config.getUntrackedParameter<edm::InputTag>("vertexLabel");
  useZMassWindow_ =  config.getUntrackedParameter<bool>("useZMassWindow");
  applyPFId_ = config.getUntrackedParameter<bool>("applyPFId", false); 
  qcdMC_ = config.getUntrackedParameter<bool>("qcdMC", false); 
  numberOfLeptons_ = config.getUntrackedParameter<unsigned int>("numberOfLeptons",1); 
  numberOfJets_ = config.getUntrackedParameter<unsigned int>("numberOfJets",1); 
  filters_ = config.getUntrackedParameter<std::vector<std::string> >("filters");
  useEventCounter_ = config.getParameter<bool>("useEventCounter");

  std::vector<edm::ParameterSet> bTagSets = config.getUntrackedParameter<std::vector<edm::ParameterSet> >("bTagSets");
  for ( int i=0, n=bTagSets.size(); i<n; ++i )
  {
    edm::ParameterSet& bTagSet = bTagSets[i];
    const std::string algo = bTagSet.getUntrackedParameter<std::string>("algo");
    const std::string name = bTagSet.getUntrackedParameter<std::string>("name");
    const double cutValue = bTagSet.getUntrackedParameter<double>("cutValue");
    const bool isCutMin = bTagSet.getUntrackedParameter<bool>("isCutMin", true); // True : reject jets with smaller than cutValue 

    std::vector<std::string>::iterator foundBtagName = std::find(bTagNames_.begin(), bTagNames_.end(), name);
    if ( foundBtagName == bTagNames_.end() )
    {
      bTagAlgos_.push_back(algo);
      bTagNames_.push_back(name);
      bTagCutValues_.push_back(cutValue);
      bTagIsCutMin_.push_back(isCutMin);
      nbjets30_.push_back(-999);
    }
    else
    {
      cout << "what is this?" << endl;
      const int index = foundBtagName - bTagNames_.begin();
      bTagAlgos_[index] = algo;
      bTagCutValues_[index] = cutValue;
      bTagIsCutMin_[index] = isCutMin;
    }
  }

  produces<std::vector<cmg::Muon> >("");

  edm::Service<TFileService> fs;

  tmp = fs->make<TH1F>("EventSummary","EventSummary",filters_.size(),0,filters_.size());

  h2_QCDMuonsIso03 = fs->make<TH2F>( "h2_QCDMuonsIso03", "h2_QCDMuonsIso03", 1000,0,10,1000, 0, 10);
  h2_QCDMuonsPt = fs->make<TH2F>( "h2_QCDMuonsPt", "h2_QCDMuonsPt", 100,0,200,100, 0, 200);
  h2_QCDMuonsEta = fs->make<TH2F>( "h2_QCDMuonsEta", "h2_QCDMuonsEta", 60,-3.0,3.0,60, -3.0, 3.0);
  h2_SIGMuonsIso03 = fs->make<TH2F>( "h2_SIGMuonsIso03", "h2_SIGMuonsIso03", 1000,0,10,1000, 0, 10);
  h2_SIGMuonsPt = fs->make<TH2F>( "h2_SIGMuonsPt", "h2_SIGMuonsPt", 100,0,200,100, 0, 200);
  h2_SIGMuonsEta = fs->make<TH2F>( "h2_SIGMuonsEta", "h2_SIGMuonsEta", 60,-3.0,3.0,60, -3.0, 3.0);
  h2_ETCMuonsIso03 = fs->make<TH2F>( "h2_ETCMuonsIso03", "h2_ETCMuonsIso03", 1000,0,10,1000, 0, 10);
  h2_ETCMuonsPt = fs->make<TH2F>( "h2_ETCMuonsPt", "h2_ETCMuonsPt", 100,0,200,100, 0, 200);
  h2_ETCMuonsEta = fs->make<TH2F>( "h2_ETCMuonsEta", "h2_ETCMuonsEta", 60,-3.0,3.0,60, -3.0, 3.0);
 
  ///////Muon loop
  for(int d=0 ; d < 3 ; d++){
    TString mainDirName = "";

    if( d == 0 ) {
       mainDirName = "Signal";
    }else if( d == 1 ) {
       mainDirName = "QCD";
    }else {
       mainDirName = "ECT";
    }
    for(int i=0 ; i < 3 ; i++){

      TString selDirName = "";
/*      if(i==0) selDirName = "Preselection";
      if(i==1) selDirName = "IDPF";
      if(i==2) selDirName = "IDLoose";
      if(i==3) selDirName = "IDTight";
      if(i==4) selDirName = "IDTightNoVtx";
*/
      if(i==0) selDirName = "IDPF";
      if(i==1) selDirName = "IDLoose";
      if(i==2) selDirName = "IDTight";

        TFileDirectory dir = fs->mkdir(Form("%s/%s",mainDirName.Data(), selDirName.Data()));

        h_pfRelIso02[d][i] = dir.make<TH1F>( "h_pfRelIso02", "h_pfRelIso02", 1000, 0, 10);
        h_pfRelIso03[d][i] = dir.make<TH1F>( "h_pfRelIso03", "h_pfRelIso03", 1000, 0, 10);
        h_pfRelIso04[d][i] = dir.make<TH1F>( "h_pfRelIso04", "h_pfRelIso04", 1000, 0, 10);
        h_pfRelIso02db[d][i] = dir.make<TH1F>( "h_pfRelIso02db", "h_pfRelIso02db", 1000, 0, 10);
        h_pfRelIso03db[d][i] = dir.make<TH1F>( "h_pfRelIso03db", "h_pfRelIso03db", 1000, 0, 10);
        h_pfRelIso03dbmod[d][i] = dir.make<TH1F>( "h_pfRelIso03dbmod", "h_pfRelIso03dbmod", 1000, 0, 10);
        h_pfRelIso04db[d][i] = dir.make<TH1F>( "h_pfRelIso04db", "h_pfRelIso04db", 1000, 0, 10);
        h_dR[d][i] = dir.make<TH1F>( "h_dR", "h_dR", 300, 0, 3);
        h_njet[d][i] = dir.make<TH1F>( "h_njet", "h_njet", 10, 0, 10);
        h_pt[d][i] = dir.make<TH1F>( "h_pt", "h_pt", 40, 0, 200);
        h_eta[d][i] = dir.make<TH1F>( "h_eta", "h_eta", 25, 0, 2.5);
        h_pv[d][i] = dir.make<TH1F>( "h_pv", "h_pv", 50, 0, 50);

        h2_pfRelIso02_vtx[d][i] = dir.make<TH2F>( "h2_pfRelIso02_vtx", "h2_pfRelIso02_vtx", 50,0,50,1000, 0, 10);
        h2_pfRelIso03_vtx[d][i] = dir.make<TH2F>( "h2_pfRelIso03_vtx", "h2_pfRelIso03_vtx", 50,0,50,1000, 0, 10);
        h2_pfRelIso04_vtx[d][i] = dir.make<TH2F>( "h2_pfRelIso04_vtx", "h2_pfRelIso04_vtx", 50,0,50,1000, 0, 10);
        h2_pfRelIso02db_vtx[d][i] = dir.make<TH2F>( "h2_pfRelIso02db_vtx", "h2_pfRelIso02db_vtx", 50,0,50,1000, 0, 10);
        h2_pfRelIso03db_vtx[d][i] = dir.make<TH2F>( "h2_pfRelIso03db_vtx", "h2_pfRelIso03db_vtx", 50,0,50,1000, 0, 10);
        h2_pfRelIso04db_vtx[d][i] = dir.make<TH2F>( "h2_pfRelIso04db_vtx", "h2_pfRelIso04db_vtx", 50,0,50,1000, 0, 10);

        h2_pfRelIso02_pt[d][i] = dir.make<TH2F>( "h2_pfRelIso02_pt", "h2_pfRelIso02_pt", 40,0,200,1000, 0, 10);
        h2_pfRelIso03_pt[d][i] = dir.make<TH2F>( "h2_pfRelIso03_pt", "h2_pfRelIso03_pt", 40,0,200,1000, 0, 10);
        h2_pfRelIso04_pt[d][i] = dir.make<TH2F>( "h2_pfRelIso04_pt", "h2_pfRelIso04_pt", 40,0,200,1000, 0, 10);
        h2_pfRelIso02db_pt[d][i] = dir.make<TH2F>( "h2_pfRelIso02db_pt", "h2_pfRelIso02db_pt", 40,0,200,1000, 0, 10);
        h2_pfRelIso03db_pt[d][i] = dir.make<TH2F>( "h2_pfRelIso03db_pt", "h2_pfRelIso03db_pt", 40,0,200,1000, 0, 10);
        h2_pfRelIso04db_pt[d][i] = dir.make<TH2F>( "h2_pfRelIso04db_pt", "h2_pfRelIso04db_pt", 40,0,200,1000, 0, 10);

        h2_pfRelIso02_eta[d][i] = dir.make<TH2F>( "h2_pfRelIso02_eta", "h2_pfRelIso02_eta", 12,-3.0,3.0,1000, 0, 10);
        h2_pfRelIso03_eta[d][i] = dir.make<TH2F>( "h2_pfRelIso03_eta", "h2_pfRelIso03_eta", 12,-3.0,3.0,1000, 0, 10);
        h2_pfRelIso04_eta[d][i] = dir.make<TH2F>( "h2_pfRelIso04_eta", "h2_pfRelIso04_eta", 12,-3.0,3.0,1000, 0, 10);
        h2_pfRelIso02db_eta[d][i] = dir.make<TH2F>( "h2_pfRelIso02db_eta", "h2_pfRelIso02db_eta", 12,-3.0,3.0,1000, 0, 10);
        h2_pfRelIso03db_eta[d][i] = dir.make<TH2F>( "h2_pfRelIso03db_eta", "h2_pfRelIso03db_eta", 12,-3.0,3.0,1000, 0, 10);
        h2_pfRelIso04db_eta[d][i] = dir.make<TH2F>( "h2_pfRelIso04db_eta", "h2_pfRelIso04db_eta", 12,-3.0,3.0,1000, 0, 10);

        h2_pfRelIso02_dimass[d][i] = dir.make<TH2F>( "h2_pfRelIso02_dimass", "h2_pfRelIso02_dimass", 200,0,200,1000, 0, 10);
        h2_pfRelIso03_dimass[d][i] = dir.make<TH2F>( "h2_pfRelIso03_dimass", "h2_pfRelIso03_dimass", 200,0,200,1000, 0, 10);
        h2_pfRelIso04_dimass[d][i] = dir.make<TH2F>( "h2_pfRelIso04_dimass", "h2_pfRelIso04_dimass", 200,0,200,1000, 0, 10);
        h2_pfRelIso02db_dimass[d][i] = dir.make<TH2F>( "h2_pfRelIso02db_dimass", "h2_pfRelIso02db_dimass", 200,0,200,1000, 0, 10);
        h2_pfRelIso03db_dimass[d][i] = dir.make<TH2F>( "h2_pfRelIso03db_dimass", "h2_pfRelIso03db_dimass", 200,0,200,1000, 0, 10);
        h2_pfRelIso04db_dimass[d][i] = dir.make<TH2F>( "h2_pfRelIso04db_dimass", "h2_pfRelIso04db_dimass", 200,0,200,1000, 0, 10);

    }
  }
  //////////////// Event loop //////////////////////
  for(int d=0 ; d < 3 ; d++){
    TString mainDirName = "";

    if( d == 0 ) {
       mainDirName = "Signal";
    }else if( d == 1 ) {
       mainDirName = "QCD";
    }else {
       mainDirName = "ECT";
    }
    TFileDirectory dir = fs->mkdir(Form("%s",mainDirName.Data()));

//    h_mtW[d]    = dir.make<TH1F>( "h_mtW", "h_mtW", 200, 0, 200);
//    h_dimass[d] = dir.make<TH1F>( "h_dimass", "h_dimass", 200, 0, 200);
    h_mtW[d]    = dir.make<TH1F>( "h_mtW", "h_mtW", 40, 0, 200);
    h_dimass[d] = dir.make<TH1F>( "h_dimass", "h_dimass", 40, 0, 200);
    h_met[d]    = dir.make<TH1F>( "h_met", "h_met", 20, 0, 200);
    h_nJet[d]   = dir.make<TH1F>( "h_nJet", "h_nJet", 10, 0, 10);
    h_nMuon[d]   = dir.make<TH1F>( "h_nMuon", "h_nMuon", 10, 0, 10);
    h_delphi[d]   = dir.make<TH1F>( "h_delphi", "h_delphi", 32, 0, 3.2);

    h_nbJet_CSVL[d] = dir.make<TH1F>("h_nbJet_CSVL","h_nbJet_CSVL",10,0,10);
    h_nbJet_CSVM[d] = dir.make<TH1F>("h_nbJet_CSVM","h_nbJet_CSVM",10,0,10);
    h_nbJet_CSVT[d] = dir.make<TH1F>("h_nbJet_CSVT","h_nbJet_CSVT",10,0,10);

  }

}

cmgMuonIsoAnalyzer::~cmgMuonIsoAnalyzer()
{

}

void cmgMuonIsoAnalyzer::produce(edm::Event& iEvent, const edm::EventSetup& es)
{
  using namespace reco;
  using namespace isodeposit;

  //const bool isRealData = iEvent.isRealData();

  EVENT  = iEvent.id().event();
  RUN    = iEvent.id().run();
  LUMI   = iEvent.id().luminosityBlock();

  edm::Handle<reco::GenParticleCollection> genParticles_;
  iEvent.getByLabel(genParticlesLabel_,genParticles_);

  iEvent.getByLabel(muonLabel_, muons_);
  iEvent.getByLabel(beamSpotLabel_,beamSpot_); 
  iEvent.getByLabel(jetLabel_, Jets);
  iEvent.getByLabel(vertexLabel_,recVtxs_);
  iEvent.getByLabel(metLabel_,MET_);
  std::vector<cmg::BaseMET>::const_iterator mi = MET_->begin();
  const double MET = mi->pt();

  std::auto_ptr<std::vector<reco::Vertex> > goodOfflinePrimaryVertices(new std::vector<reco::Vertex>());
  int nvertex = 0 ;
  for(unsigned int i=0; i < recVtxs_->size();  ++i){
    reco::Vertex v = recVtxs_->at(i);
    if (!(v.isFake()) && (v.ndof()>4) && (fabs(v.z())<=24.0) && (v.position().Rho()<=2.0) ) {
      goodOfflinePrimaryVertices->push_back((*recVtxs_)[i]);
      nvertex++;
    }
  }

  std::auto_ptr<std::vector<cmg::Muon> > triggeredMuons(new std::vector<cmg::Muon>());

  //preselection
  for (unsigned int i=0; i < muons_->size(); ++i){
    cmg::Muon muon = muons_->at(i);

    ////use dxy with respect to beamspot
    //bool passPre = muon.pt() > 20 && fabs(muon.eta()) < 2.5 && fabs(muon.gsfTrack()->dxy(beamSpot_->position())) < 0.04;
    //// use dxy with respect to PV
    if( nvertex < 1 ) continue;
    //reco::Vertex pv = goodOfflinePrimaryVertices->at(0);
    //bool passPre = muon.pt() > 20 && fabs(muon.eta()) < 2.5 && fabs( muon.sourcePtr()->get()->gsfTrack()->dxy(pv.position()) ) < 0.04;
    bool passPre = muon.pt() > 20 && fabs(muon.eta()) < 2.5;
    bool passPF = muon.isPF(); 
    //bool passPF = muon.sourcePtr()->get()->isPF();
    //bool passTrig = passPre && muon.getSelection("cuts_premvaTrig"); //->get());
    ////////////////////////////////////////////////////////////////////////////////////////
    //bool passTrig = passPre && trainTrigPresel(muon, numberOfHits_ ); 
    ////////////////////////////////////////////////////////////////////////////////////////
    //bool passTrig = passPre; 

    if( !passPre ) continue; 
    if( applyPFId_ ){
      if( !passPF ) continue;
    }

    triggeredMuons->push_back((*muons_)[i]);
  }
 
  std::auto_ptr<std::vector<cmg::PFJet> > cleanedJets(new std::vector<cmg::PFJet>());

  for ( int bTagIndex=0, nBTag=nbjets30_.size(); bTagIndex<nBTag; ++bTagIndex )
  {
    nbjets30_[bTagIndex] = 0;
  }

  for (unsigned int j=0 ; j < Jets->size(); j++) {
    cmg::PFJet jet = Jets->at(j);

    bool passLooseJetId = jet.getSelection("cuts_looseJetId");

    if( !passLooseJetId ) continue;
    if( !(jet.pt() > 30 && abs(jet.eta()) < 2.5) ) continue;

    bool overlap = false;
/////////////////    
    //cout << "==============================================================" << endl;
    for ( int bTagIndex=0, nBTagAlgo=bTagAlgos_.size(); bTagIndex<nBTagAlgo; ++bTagIndex )
    {
      const double bTagValue = (*Jets)[j].bDiscriminator(bTagAlgos_[bTagIndex].c_str());
      if ( (bTagIsCutMin_[bTagIndex]) xor (bTagValue < bTagCutValues_[bTagIndex]) ) ++nbjets30_[bTagIndex];
    //cout << "nbjets30 (" << bTagIndex << ")" << nbjets30_[bTagIndex] << endl; 
    }
/////////////////    
        for (unsigned int i=0; i < triggeredMuons->size(); ++i){
      cmg::Muon muon = triggeredMuons->at(i);
      double dR =  deltaR(muon.eta(), muon.phi(), jet.eta(), jet.phi());
      if( dR < 0.5 ) {
        overlap = true;
        break;
      }
    }

    if( !overlap ) cleanedJets->push_back( (*Jets)[j] );
  }

  int nJets = cleanedJets->size();
  int nMuons = triggeredMuons->size();

  double mtW = -1.0;
  double delphi = -1.0;
  if( triggeredMuons->size() >=1) {
    const cmg::Muon leading = triggeredMuons->at(0);
    mtW =  transverseMass( leading.p4() , mi->p4() );
    delphi = fabs(deltaPhi(leading.phi(), mi->p4().phi()));
  }

  double dimass = -1.;
  double charge = -1.;
  double relPfIso03leg1 = -1.; 
  double relPfIso03leg2 = -1.;
  bool SIG = false; 
  bool QCD = false; 
  cmg::Muon muon1;
  cmg::Muon muon2;
 
  for( unsigned int i = 0 ; i < triggeredMuons->size() ; i++){
    for( unsigned int j = 0 ; j < triggeredMuons->size() ; j++){

      muon1 = triggeredMuons->at(i);
      muon2 = triggeredMuons->at(j);
      const bool match = MatchObjects( muon1.p4(), muon2.p4(), true);
      if(match) continue; 

      if(disc.Rndm()>0.5){
      muon2 = triggeredMuons->at(i);
      muon1 = triggeredMuons->at(j);
      }

      dimass = (muon1.p4() + muon2.p4()).M();
      charge = muon1.charge()*muon2.charge();

      double chIso03muon1 = muon1.chargedHadronIso(0.3);
      double puChIso03muon1 = muon1.puChargedHadronIso(0.3);
      double nhIso03muon1 = muon1.neutralHadronIso(0.3);
      double phIso03muon1 = muon1.photonIso(0.3);
      relPfIso03leg1 = ( chIso03muon1 + max(0.0, nhIso03muon1 + phIso03muon1 - 0.5*puChIso03muon1) )/ muon1.pt();
      //relPfIso03leg1 = ( chIso03muon1 + nhIso03muon1 + phIso03muon1 )/ muon1.pt();

      double chIso03muon2 = muon2.chargedHadronIso(0.3);
      double puChIso03muon2 = muon2.puChargedHadronIso(0.3);
      double nhIso03muon2 = muon2.neutralHadronIso(0.3);
      double phIso03muon2 = muon2.photonIso(0.3);
      relPfIso03leg2 = ( chIso03muon2 + max(0.0, nhIso03muon2 + phIso03muon2 - 0.5*puChIso03muon2) )/ muon2.pt();
      //relPfIso03leg2 = ( chIso03muon2 + nhIso03muon2 + phIso03muon2 )/ muon2.pt();
 
      break;
    }
  }

  //// SIG EVENT selection ////
  bool SIG0 = true ;
  bool SIG1 = true ;
  bool SIG2 = true ;
  bool SIG3 = true ;
  bool SIG4 = true ;
  bool SIG5 = true ;
  //SIG0 = mtW >= 40 ;
  //SIG1 = dimass > 12 && fabs(dimass-91) > 15;
  //SIG2 = relPfIso03leg2 <= 0.15;
  //SIG3 = charge < 0;
  //SIG4 = MET >= 30;
  //SIG5 = nbjets30_[0] >= 2;// 0=CSVL, 1=CSVM 
//  SIG5 = nJets >= 2 && nbjets30_[1] >= 1;// 0=CSVL, 1=CSVM 
  SIG5 = nJets >= 2 ;// 0=CSVL, 1=CSVM 

  SIG = SIG0 && SIG1 && SIG2 && SIG3 && SIG4 && SIG5;

  //// QCD EVENT selection ////
  //bool QCD1 = dimass > 12 ;
  //bool QCD1 = fabs(dimass-91) > 20 ;
  bool QCD0 = true ;
  bool QCD1 = true ;
  bool QCD2 = true ;
  bool QCD3 = true ;
  bool QCD4 = true ;
  bool QCD5 = true ;
  QCD0 = dimass > 12 && fabs(dimass-91) > 15;
  QCD1 = mtW<40 ;
  QCD2 = relPfIso03leg2 > 0.25 ;
  QCD3 = charge > 0;
  QCD4 = MET < 30;
  //QCD5 = nJets >= 0;

  if(qcdMC_){
    QCD = true ;
  }else{
    QCD = QCD0 && QCD1 && QCD2 && QCD3 && QCD4 && QCD5 ; 
  }

  int d;

  if(QCD ) {
    d=1;
    h2_QCDMuonsIso03->Fill( relPfIso03leg1, relPfIso03leg2 );
    h2_QCDMuonsPt->Fill( muon1.pt(), muon2.pt() );  
    h2_QCDMuonsEta->Fill( muon1.eta(), muon2.eta() );  
  } else if(SIG ) {
    d=0;
    h2_SIGMuonsIso03->Fill( relPfIso03leg1, relPfIso03leg2 );
    h2_SIGMuonsPt->Fill( muon1.pt(), muon2.pt() );  
    h2_SIGMuonsEta->Fill( muon1.eta(), muon2.eta() );  
  }else {
    d=2;
    h2_ETCMuonsIso03->Fill( relPfIso03leg1, relPfIso03leg2 );
    h2_ETCMuonsPt->Fill( muon1.pt(), muon2.pt() );  
    h2_ETCMuonsEta->Fill( muon1.eta(), muon2.eta() );  
  }

  bool eventsel = triggeredMuons->size() >= numberOfLeptons_ && nJets >=  (int) numberOfJets_ ;
//  bool eventsel = triggeredMuons->size() >= numberOfLeptons_  ;

  if( eventsel ){
    h_mtW[d]->Fill(mtW);
    h_dimass[d]->Fill(dimass);
    h_met[d]->Fill(MET);
    h_nJet[d]->Fill(nJets);
    h_nMuon[d]->Fill(nMuons);
    h_delphi[d]->Fill(delphi);
  } 
// Muon loop
//  for (unsigned int j=0; j < triggeredMuons->size() && eventsel ; ++j){
  for (unsigned int j=0; j < 2 && eventsel ; ++j){
    cmg::Muon Lep1 = triggeredMuons->at(j);
//  if (eventsel ){
    double pt1  = Lep1.pt();
    double sceta1 = Lep1.eta();
   
    double chIso02Lep1 = Lep1.chargedHadronIso(0.2);
    double puChIso02Lep1 = Lep1.puChargedHadronIso(0.2);
    double nhIso02Lep1 = Lep1.neutralHadronIso(0.2);
    double phIso02Lep1 = Lep1.photonIso(0.2);

    double chIso03Lep1 = Lep1.chargedHadronIso(0.3);
    double puChIso03Lep1 = Lep1.puChargedHadronIso(0.3);
    double nhIso03Lep1 = Lep1.neutralHadronIso(0.3);
    double phIso03Lep1 = Lep1.photonIso(0.3);
  
    double chIso04Lep1 = Lep1.chargedHadronIso(0.4);
    double puChIso04Lep1 = Lep1.puChargedHadronIso(0.4);
    double nhIso04Lep1 = Lep1.neutralHadronIso(0.4);
    double phIso04Lep1 = Lep1.photonIso(0.4);
    double sf = 0.5;
    if( fabs(sceta1) > 2.1 ) sf = 1.0; 
    double relPfIso02Lep1 = ( chIso02Lep1 + nhIso02Lep1 + phIso02Lep1 )/ Lep1.pt(); 
    double relPfIso03Lep1 = ( chIso03Lep1 + nhIso03Lep1 + phIso03Lep1 )/ Lep1.pt(); 
    double relPfIso04Lep1 = ( chIso04Lep1 + nhIso04Lep1 + phIso04Lep1 )/ Lep1.pt();
    double relPfIso02dbLep1 = ( chIso02Lep1 + max(0.0, nhIso02Lep1 + phIso02Lep1 - 0.5*puChIso02Lep1) )/ Lep1.pt();
    double relPfIso03dbLep1 = ( chIso03Lep1 + max(0.0, nhIso03Lep1 + phIso03Lep1 - 0.5*puChIso03Lep1) )/ Lep1.pt();
    double relPfIso03dbmodLep1 = ( max(0.0, chIso03Lep1 + nhIso03Lep1 + phIso03Lep1 - sf*puChIso03Lep1) )/ Lep1.pt();
    double relPfIso04dbLep1 = ( chIso04Lep1 + max(0.0, nhIso04Lep1 + phIso04Lep1 - 0.5*puChIso04Lep1) )/ Lep1.pt();
    double dRLep1 = 999;

    for (unsigned jid = 0; jid < cleanedJets->size(); jid++){
      cmg::PFJet jet = cleanedJets->at(jid);
      double dRval = deltaR(Lep1.eta(), Lep1.phi(), jet.eta(), jet.phi());
      if( dRval < dRLep1 ) dRLep1 = dRval;
      break;//consider only leading jet
    }

    //////////////////////////
    /////for selections //////
    //////////////////////////

    bool passPF         = Lep1.isPF();
    bool passLoose      = Lep1.getSelection("cuts_loosemuon");
    bool passTight      = Lep1.getSelection("cuts_tightmuonNoVtx") && Lep1.dxy()<0.2 && Lep1.dz()<0.5 ;
    //bool passTightNoVtx = Lep1.getSelection("cuts_tightmuonNoVtx");

    for( int sel = 0 ; sel < 3 ; sel++){

      bool fill = true;
/*      if( sel == 1 ) fill = passPF;
      if( sel == 2 ) fill = passLoose;
      if( sel == 3 ) fill = passTight;
      if( sel == 4 ) fill = passTightNoVtx;
*/
      if( sel == 0 ) fill = passPF;
      if( sel == 1 ) fill = passLoose;
      if( sel == 2 ) fill = passTight;

      if( fill ){
        h_pfRelIso02[d][sel]->Fill( relPfIso02Lep1 );
        h_pfRelIso03[d][sel]->Fill( relPfIso03Lep1 );
        h_pfRelIso04[d][sel]->Fill( relPfIso04Lep1 );
        h_pfRelIso02db[d][sel]->Fill( relPfIso02dbLep1 );
        h_pfRelIso03db[d][sel]->Fill( relPfIso03dbLep1 );
        h_pfRelIso03dbmod[d][sel]->Fill( relPfIso03dbmodLep1 );
        h_pfRelIso04db[d][sel]->Fill( relPfIso04dbLep1 );

        if( nJets >= 1 ) h_dR[d][sel]->Fill(dRLep1);
        h_njet[d][sel]->Fill(nJets);
        h_pt[d][sel]->Fill(pt1);
        h_eta[d][sel]->Fill(sceta1);
        h_pv[d][sel]->Fill(nvertex);

        h2_pfRelIso02_vtx[d][sel]->Fill( nvertex, relPfIso02Lep1 );
        h2_pfRelIso03_vtx[d][sel]->Fill( nvertex, relPfIso03Lep1 );
        h2_pfRelIso04_vtx[d][sel]->Fill( nvertex, relPfIso04Lep1 );
        h2_pfRelIso02db_vtx[d][sel]->Fill(nvertex, relPfIso02dbLep1 );
        h2_pfRelIso03db_vtx[d][sel]->Fill(nvertex, relPfIso03dbLep1 );
        h2_pfRelIso04db_vtx[d][sel]->Fill( nvertex, relPfIso04dbLep1 );

        h2_pfRelIso02_pt[d][sel]->Fill( Lep1.pt(), relPfIso02Lep1 );
        h2_pfRelIso03_pt[d][sel]->Fill( Lep1.pt(), relPfIso03Lep1 );
        h2_pfRelIso04_pt[d][sel]->Fill( Lep1.pt(), relPfIso04Lep1 );
        h2_pfRelIso02db_pt[d][sel]->Fill(Lep1.pt(), relPfIso02dbLep1 );
        h2_pfRelIso03db_pt[d][sel]->Fill(Lep1.pt(), relPfIso03dbLep1 );
        h2_pfRelIso04db_pt[d][sel]->Fill( Lep1.pt(), relPfIso04dbLep1 );

        h2_pfRelIso02_eta[d][sel]->Fill( Lep1.eta(), relPfIso02Lep1 );
        h2_pfRelIso03_eta[d][sel]->Fill( Lep1.eta(), relPfIso03Lep1 );
        h2_pfRelIso04_eta[d][sel]->Fill( Lep1.eta(), relPfIso04Lep1 );
        h2_pfRelIso02db_eta[d][sel]->Fill(Lep1.eta(), relPfIso02dbLep1 );
        h2_pfRelIso03db_eta[d][sel]->Fill(Lep1.eta(), relPfIso03dbLep1 );
        h2_pfRelIso04db_eta[d][sel]->Fill( Lep1.eta(), relPfIso04dbLep1 );

        h2_pfRelIso02_dimass[d][sel]->Fill( dimass, relPfIso02Lep1 );
        h2_pfRelIso03_dimass[d][sel]->Fill( dimass, relPfIso03Lep1 );
        h2_pfRelIso04_dimass[d][sel]->Fill( dimass, relPfIso04Lep1 );
        h2_pfRelIso02db_dimass[d][sel]->Fill(dimass, relPfIso02dbLep1 );
        h2_pfRelIso03db_dimass[d][sel]->Fill(dimass, relPfIso03dbLep1 );
        h2_pfRelIso04db_dimass[d][sel]->Fill( dimass, relPfIso04dbLep1 );
      }
    }
    //break;
  } //muon loop

  iEvent.put(triggeredMuons);
 
}

void 
cmgMuonIsoAnalyzer::beginJob(){

}

void
cmgMuonIsoAnalyzer::endJob() {
}

double cmgMuonIsoAnalyzer::transverseMass( const reco::Candidate::LorentzVector& lepton,
                                     const reco::Candidate::LorentzVector& met) {

  reco::Candidate::LorentzVector leptonT(lepton.Px(),lepton.Py(),0.,lepton.E()*sin(lepton.Theta()));
  reco::Candidate::LorentzVector sumT=leptonT+met;
  return std::sqrt(sumT.M2());
}

bool cmgMuonIsoAnalyzer::isFromWorZ( const reco::Candidate::LorentzVector& lepton, const edm::Handle<reco::GenParticleCollection> & genParticles_ ){

  bool out = false;

  for (reco::GenParticleCollection::const_iterator mcIter=genParticles_->begin(); mcIter != genParticles_->end(); mcIter++ ) {
    int genId = mcIter->pdgId();

    if( abs(genId) != 13 ) continue;

    bool match = MatchObjects(lepton, mcIter->p4(), false);

    if( match != true) continue;
   
    const reco::Candidate* mother = mcIter->mother();
    while( mother != 0 ){
      //if( abs(mother->pdgId()) == 24 || abs(mother->pdgId()) == 23 ) { 
      if( abs(mother->pdgId()) == 24 || abs(mother->pdgId()) == 23 || abs(mother->pdgId()) == 15) { 
        out = true;
      }
      mother = mother->mother();
    }
  }

  return out;
}

bool cmgMuonIsoAnalyzer::MatchObjects( const reco::Candidate::LorentzVector& pasObj,
      const reco::Candidate::LorentzVector& proObj,
      bool exact ) {
    double proEta = proObj.eta();
    double proPhi = proObj.phi();
    double proPt  = proObj.pt();
    double pasEta = pasObj.eta();
    double pasPhi = pasObj.phi();
    double pasPt  = pasObj.pt();

    double dRval = deltaR(proEta, proPhi, pasEta, pasPhi);
    double dPtRel = 999.0;
    if( proPt > 0.0 ) dPtRel = fabs( pasPt - proPt )/proPt;
    // If we are comparing two objects for which the candidates should
    // be exactly the same, cut hard. Otherwise take cuts from user.
    if( exact ) return ( dRval < 1e-3 && dPtRel < 1e-3 );
    else        return ( dRval < 0.025 && dPtRel < 0.025 );
}

void cmgMuonIsoAnalyzer::endLuminosityBlock(edm::LuminosityBlock & lumi, const edm::EventSetup & setup){
  if(useEventCounter_){
    for(unsigned int i=0;i<filters_.size();++i) {
      std::string name = filters_[i];
      edm::Handle<edm::MergeableCounter> numEventsCounter;
      lumi.getByLabel(name, numEventsCounter);
      if( numEventsCounter.isValid()){
        tmp->AddBinContent(i+1, numEventsCounter->value);
        tmp->GetXaxis()->SetBinLabel(i+1,filters_[i].c_str());
      }
    }
  }
//  return true;
}



////////////////
#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(cmgMuonIsoAnalyzer);



