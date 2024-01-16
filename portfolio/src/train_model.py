from models.model import Models
from sklearn.model_selection import GridSearchCV
from skfolio.model_selection import  WalkForward
from skfolio.moments import EmpiricalCovariance, LedoitWolf
from skfolio import RatioMeasure, RiskMeasure
from skfolio.metrics import make_scorer
import os
import pandas as pd
import dill as pickle

class ModelTrainer:
    def __init__(self):
        self.models = Models()
        self.model_stacking = self.models.give_model_stacking()
        self.benchmark = self.models.give_benchmark()

    def tune_parameters(self):
        self.cv = WalkForward(train_size=252, test_size=60)
        self.grid_search = GridSearchCV(
            estimator=self.model_stacking,
            cv=self.cv,
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

    def train(self, X_train):
        self.grid_search.fit(X_train)
        self.model_stacking = self.grid_search.best_estimator_

    def save_model(self, model_path, benchmark_path):
        with open(model_path, 'wb') as file:
            pickle.dump(self.model_stacking, file)
        with open(benchmark_path, 'wb') as file:
            pickle.dump(self.benchmark, file)

def main():
    # Initialize the model trainer
    trainer = ModelTrainer()

    # Tune the parametersdocker push gcr.io/mlops-411012/trainer
    trainer.tune_parameters()

    # Check if running inside a Docker container
    if os.environ.get('RUNNING_IN_DOCKER'):
        data_path = '/data/processed/X_train.csv'
        model_path = '/models/model.pkl'
        benchmark_path = '/models/benchmark.pkl'
    else:
        script_dir = os.path.dirname(__file__)
        data_path = os.path.join(script_dir, '../data/processed/X_train.csv')
        model_dir = os.path.join(script_dir, '../models/')
        model_path = os.path.join(model_dir, 'model.pkl')
        benchmark_path = os.path.join(model_dir, 'benchmark.pkl')

    # Load the training data
    X_train = pd.read_csv(data_path, index_col=0)

    # Train the model
    trainer.train(X_train)

    # Save the model
    trainer.save_model(model_path, benchmark_path)

if __name__ == "__main__":
    main()