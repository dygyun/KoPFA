#ifndef METCandidate_H
#define METCandidate_H

#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/PatCandidates/interface/Lepton.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "TLorentzVector.h"

namespace Ko{

  typedef reco::Candidate::LorentzVector LorentzVector;

  class METCandidate : public LorentzVector{
  public:
    METCandidate(){}
    virtual ~METCandidate(){}

    METCandidate(const reco::Candidate::LorentzVector& p4);
    const double pt() const { return pt_; }
    const double eta() const { return eta_; }
    METCandidate(double MET, double sumEt, double photonEtFrac, double neutralHadEtFrac, double chargedHadEtFrac, double electronEtFrac, double muonEtFrac) {
      MET_ = MET;
      sumEt_ = sumEt;
      photonEt_ = sumEt * photonEtFrac;
      neutralHadEt_ = sumEt * neutralHadEtFrac;
      chargedHadEt_ = sumEt * chargedHadEtFrac;
      electronEt_ = sumEt * electronEtFrac;
      muonEt_ = sumEt * muonEtFrac;
    }

    const double et() const { return MET_; }
    const double sumEt() const { return sumEt_; }
    const double photonEt() const { return photonEt_; }
    const double neutralHadEt() const { return neutralHadEt_; }
    const double chargedHadEt() const { return chargedHadEt_; } 
    const double electronEt() const { return electronEt_; }
    const double muonEt() const { return muonEt_; }

  private:

    double pt_;
	double eta_;
	double MET_;
    double sumEt_;
    double photonEt_;
    double neutralHadEt_;
    double chargedHadEt_;
    double electronEt_;
    double muonEt_;

  };



}
#endif
