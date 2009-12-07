
#ifndef STEIHAUGSR1_H

#include <otkpp/linalg/SR1Updater.h>
#include <otkpp/localsolvers/native/GradientSolver.h>
#include <otkpp/localsolvers/native/trsreg/SteihaugSolver.h>

/// Implements the BFGS algorithm with Steihaug's trust region method.
class SteihaugSR1 : public GradientSolver
{
 public:
  struct State : public Cloneable< State, GradientSolver::State > { };
  
  SteihaugSR1();
  ~SteihaugSR1();

  std::string getName() const;
  const State &getState() const { return state_; }
  bool usesGradient() const;
  bool usesHessian() const;
 private:
  matrix< double > H_;
  SR1Updater matrixUpdater_;
  vector< double > p_;
  vector< double > q_;
  State state_;
  SteihaugSolver trSolver_;
  
  IterationStatus iterate_();
  void setup_(const Function &objFunc,
              const vector< double > &x0,
              const Solver::Setup &solverSetup,
              const Constraints &C);
};

#define STEIHAUGSR1_H

#endif
