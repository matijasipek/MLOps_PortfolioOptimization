from skfolio import RiskMeasure
from skfolio.optimization import (
    EqualWeighted,
    HierarchicalEqualRiskContribution,
    InverseVolatility,
    MaximumDiversification,
    MeanRisk,
    ObjectiveFunction,
    StackingOptimization,
)
from skfolio.prior import EmpiricalPrior


class Models():
    def give_estimators(self):
        estimators = [
            ("model1", InverseVolatility()),
            ("model2", MaximumDiversification(prior_estimator=EmpiricalPrior())),
            (
                "model3",
                MeanRisk(objective_function=ObjectiveFunction.MAXIMIZE_UTILITY, min_weights=-1),
            ),
            ("model4", HierarchicalEqualRiskContribution()),
        ]
        return estimators

    def give_model_stacking(self):
        estimators = self.give_estimators()
        model_stacking = StackingOptimization(
            estimators=estimators,
            final_estimator=MeanRisk(
                objective_function=ObjectiveFunction.MAXIMIZE_UTILITY,
                risk_measure=RiskMeasure.CDAR,
            ),
        )

        return model_stacking

    def give_benchmark(self):
        benchmark = EqualWeighted()
        return benchmark
    
