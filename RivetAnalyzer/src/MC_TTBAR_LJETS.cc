#include "Rivet/Analysis.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/ChargedLeptons.hh"
#include "Rivet/Projections/FastJets.hh"
#include "Rivet/AnalysisLoader.hh"
#include "Rivet/RivetAIDA.hh"


namespace Rivet {

  class MC_TTBAR_LJETS : public Analysis {

  public:

    MC_TTBAR_LJETS()
      : Analysis("MC_TTBAR_LJETS")
    {
      _sumwPassedLepJetMET = 0;
      _sumwPassedJetID = 0;
      _sumwPassedWMass = 0;
    
    }


    /// @name Analysis methods
    //@{

    void init() {
      addProjection(ChargedLeptons(FinalState(-4.2, 4.2, 30*GeV)), "LFS");
      addProjection(FastJets(FinalState(-4.2, 4.2, 0*GeV), FastJets::ANTIKT, 0.4), "Jets");

      _h_njets = bookHistogram1D("mult_alljet", 11, -0.5, 10.5);
      _h_bjets = bookHistogram1D("mult_bjet", 11, -0.5, 10.5);
      _h_ljets = bookHistogram1D("mult_ljet", 11, -0.5, 10.5);

      _h_jet_1_pT = bookHistogram1D("jet_1_pT", 50, 0, 500);
      _h_jet_2_pT = bookHistogram1D("jet_2_pT", 50, 0, 400);
      _h_jet_3_pT = bookHistogram1D("jet_3_pT", 50, 0, 300);
      _h_jet_4_pT = bookHistogram1D("jet_4_pT", 50, 0, 200);

      _h_bjet_1_pT = bookHistogram1D("jetb_1_pT", 50, 0, 250);
      _h_bjet_2_pT = bookHistogram1D("jetb_2_pT", 50, 0, 250);

      _h_ljet_1_pT = bookHistogram1D("jetl_1_pT", 50, 0, 250);
      _h_ljet_2_pT = bookHistogram1D("jetl_2_pT", 50, 0, 250);

      _h_W_mass = bookHistogram1D("W_mass", 75, 0, 500);
      _h_t_mass = bookHistogram1D("t_mass", 75, 0, 1400);
      _h_ttbar_mass = bookHistogram1D("ttbar_mass", 75, 0, 1400);
      _h_t_mass_W_cut = bookHistogram1D("t_mass_W_cut", 75, 0, 1400);
      _h_W_comb_mass = bookHistogram1D("W_comb_mass", 75, 0, 500);
      _h_t_comb_mass = bookHistogram1D("t_comb_mass", 75, 0, 1400);
    }


    void analyze(const Event& event) {
      const double weight = event.weight();

      const ChargedLeptons& lfs = applyProjection<ChargedLeptons>(event, "LFS");
      MSG_DEBUG("Charged lepton multiplicity = " << lfs.chargedLeptons().size());
      foreach (Particle lepton, lfs.chargedLeptons()) {
        MSG_DEBUG("Lepton pT = " << lepton.momentum().pT());
      }
      if (lfs.chargedLeptons().empty()) {
        MSG_DEBUG("Event failed lepton multiplicity cut");
        vetoEvent;
      }

      const FastJets& jetpro = applyProjection<FastJets>(event, "Jets");
      const Jets alljets = jetpro.jetsByPt();
      if (alljets.size() < 4) {
        MSG_DEBUG("Event failed jet multiplicity cut");
        vetoEvent;
      }
      _sumwPassedLepJetMET += weight;
      _h_jet_1_pT->fill(alljets[0].momentum().pT(), weight);
      _h_jet_2_pT->fill(alljets[1].momentum().pT(), weight);
      _h_jet_3_pT->fill(alljets[2].momentum().pT(), weight);
      _h_jet_4_pT->fill(alljets[3].momentum().pT(), weight);

      const Jets jets = jetpro.jetsByPt(35*GeV);
      _h_njets->fill(jets.size(), weight);
      foreach (const Jet& jet, jets) {
        MSG_DEBUG("Jet pT = " << jet.momentum().pT()/GeV << " GeV");
      }
      if (jets.size() < 4) {
        MSG_DEBUG("Event failed jet pT cut");
        vetoEvent;
      }

      Jets bjets, ljets;
      foreach (const Jet& jet, jets) {
        if (jet.containsBottom()) {
          bjets.push_back(jet);
        } else {
          ljets.push_back(jet);
        }
      }
      _h_bjets->fill(bjets.size(), weight);
      _h_ljets->fill(ljets.size(), weight);
      MSG_DEBUG("Number of b-jets = " << bjets.size());
      if (bjets.size() != 2) {
        MSG_DEBUG("Event failed b-tagging cut");
        vetoEvent;
      }
      _sumwPassedJetID += weight;
      _h_bjet_1_pT->fill(bjets[0].momentum().pT(), weight);
      _h_bjet_2_pT->fill(bjets[1].momentum().pT(), weight);
      _h_ljet_1_pT->fill(ljets[0].momentum().pT(), weight);
      _h_ljet_2_pT->fill(ljets[1].momentum().pT(), weight);

      const FourMomentum W  = ljets[0].momentum() + ljets[1].momentum();
      const FourMomentum t1 = W + bjets[0].momentum();
      const FourMomentum t2 = W + bjets[1].momentum();
      const FourMomentum ttbar = t1 + t2;

      _h_W_mass->fill(W.mass(), weight);
      _h_t_mass->fill(t1.mass(), weight);
      _h_t_mass->fill(t2.mass(), weight);
      _h_ttbar_mass->fill(ttbar.mass(), weight);
      if (inRange(W.mass()/GeV, 70, 90)) {
        MSG_DEBUG("W found with mass " << W.mass()/GeV << " GeV");
        _sumwPassedWMass += weight;
        _h_t_mass_W_cut->fill(t1.mass(), weight);
        _h_t_mass_W_cut->fill(t2.mass(), weight);
      }

      // All combinatoric 2-jet masses
      _h_W_comb_mass->fill(mass(jets[0].momentum() + jets[1].momentum()), weight);
      _h_W_comb_mass->fill(mass(jets[0].momentum() + jets[2].momentum()), weight);
      _h_W_comb_mass->fill(mass(jets[0].momentum() + jets[3].momentum()), weight);
      _h_W_comb_mass->fill(mass(jets[1].momentum() + jets[2].momentum()), weight);
      _h_W_comb_mass->fill(mass(jets[1].momentum() + jets[3].momentum()), weight);
      _h_W_comb_mass->fill(mass(jets[2].momentum() + jets[3].momentum()), weight);

      // All combinatoric 3-jet masses
      _h_t_comb_mass->fill(mass(jets[0].momentum() + jets[1].momentum() + jets[2].momentum()), weight);
      _h_t_comb_mass->fill(mass(jets[0].momentum() + jets[1].momentum() + jets[3].momentum()), weight);
      _h_t_comb_mass->fill(mass(jets[0].momentum() + jets[2].momentum() + jets[3].momentum()), weight);
      _h_t_comb_mass->fill(mass(jets[1].momentum() + jets[2].momentum() + jets[3].momentum()), weight);

      /// @todo Add reconstruction of the other top from the leptonically decaying W, using WFinder
    }


    void finalize() {
      // No histos, so nothing to do!
      cout << "_sumwPassedLepJetMET = " << _sumwPassedLepJetMET << endl;
      cout << "_sumwPassedJetID = " << _sumwPassedJetID << endl;
      cout << "_sumwPassedWMass = " << _sumwPassedWMass <<endl;
    }

    //@}


  private:

    double _sumwPassedLepJetMET, _sumwPassedJetID, _sumwPassedWMass;

    AIDA::IHistogram1D *_h_njets, *_h_bjets, *_h_ljets;
    AIDA::IHistogram1D *_h_jet_1_pT, *_h_jet_2_pT, *_h_jet_3_pT, *_h_jet_4_pT;
    AIDA::IHistogram1D *_h_bjet_1_pT, *_h_bjet_2_pT;
    AIDA::IHistogram1D *_h_ljet_1_pT, *_h_ljet_2_pT;
    AIDA::IHistogram1D *_h_W_mass;
    AIDA::IHistogram1D *_h_t_mass;
    AIDA::IHistogram1D *_h_ttbar_mass;
    AIDA::IHistogram1D *_h_W_comb_mass;
    AIDA::IHistogram1D *_h_t_comb_mass;
    AIDA::IHistogram1D *_h_t_mass_W_cut;

  };


  // This global object acts as a hook for the plugin system
  AnalysisBuilder<MC_TTBAR_LJETS> plugin_MC_TTBAR_LJETS;

}


