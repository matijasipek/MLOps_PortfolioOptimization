from plotly.io import show
from sklearn.model_selection import GridSearchCV, train_test_split

from skfolio import Population, RatioMeasure, RiskMeasure
from skfolio.datasets import load_ftse100_dataset
from skfolio.metrics import make_scorer
from skfolio.model_selection import (
    CombinatorialPurgedCV,
    WalkForward,
    cross_val_predict,
)
from skfolio.moments import EmpiricalCovariance, LedoitWolf
from skfolio.optimization import (
    EqualWeighted,
    HierarchicalEqualRiskContribution,
    InverseVolatility,
    MaximumDiversification,
    MeanRisk,
    ObjectiveFunction,
    StackingOptimization,
)
from skfolio.preprocessing import prices_to_returns
from skfolio.prior import EmpiricalPrior

import matplotlib.pyplot as plt
from plotly.io import write_image

import pandas as pd
import os


### DATA
# DATA
script_dir = os.path.dirname(__file__)  # get the directory of the current script
rel_path = '../../data/raw/ftse100_dataset.csv.gz'
abs_file_path = os.path.join(script_dir, rel_path)
prices_raw = pd.read_csv(abs_file_path)
print(prices_raw)

prices = load_ftse100_dataset()
X = prices_to_returns(prices)
#X_train, X_test = train_test_split(X, test_size=0.50, shuffle=False)

X_train, X_test = train_test_split(X, test_size=0.50, shuffle=False)



### MODELS
estimators = [
    ("model1", InverseVolatility()),
    ("model2", MaximumDiversification(prior_estimator=EmpiricalPrior())),
    (
        "model3",
        MeanRisk(objective_function=ObjectiveFunction.MAXIMIZE_UTILITY, min_weights=-1),
    ),
    ("model4", HierarchicalEqualRiskContribution()),
]

model_stacking = StackingOptimization(
    estimators=estimators,
    final_estimator=MeanRisk(
        objective_function=ObjectiveFunction.MAXIMIZE_UTILITY,
        risk_measure=RiskMeasure.CDAR,
    ),
)

### BENCHMARK
benchmark = EqualWeighted()


### PARAMETER TUNING
cv = WalkForward(train_size=252, test_size=60)

grid_search = GridSearchCV(
    estimator=model_stacking,
    cv=cv,
    n_jobs=-1,
    param_grid={
        "model2__prior_estimator__covariance_estimator": [
            EmpiricalCovariance(),
            LedoitWolf(),
        ],
        "model3__l1_coef": [0.001, 0.1],
        "model4__risk_measure": [
            RiskMeasure.VARIANCE,
            RiskMeasure.GINI_MEAN_DIFFERENCE,
        ],
    },
    scoring=make_scorer(RatioMeasure.CALMAR_RATIO),
)
grid_search.fit(X_train)
model_stacking = grid_search.best_estimator_
print("Model stacking " , model_stacking)


### PREDICTION
pred_bench = cross_val_predict(
    benchmark,
    X_test,
    cv=cv,
    portfolio_params=dict(name="Benchmark"),
)

pred_stacking = cross_val_predict(
    model_stacking,
    X_test,
    cv=cv,
    n_jobs=-1,
    portfolio_params=dict(name="Stacking"),
)

print("pred_bench", pred_bench)
print("pred_stacking", pred_stacking)


### POPULATION ANALYSIS
population = Population([pred_bench, pred_stacking])

# Plot cumulative returns and save the figure
fig1 = population.plot_cumulative_returns()
fig1.show()