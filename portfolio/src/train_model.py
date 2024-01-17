from models.model import Models
from sklearn.model_selection import GridSearchCV
from skfolio.model_selection import  WalkForward
from skfolio.moments import EmpiricalCovariance, LedoitWolf
from skfolio import RatioMeasure, RiskMeasure
from skfolio.metrics import make_scorer
import os
import wandb
import yaml
import pandas as pd
import dill as pickle
import cProfile
import pstats

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
        #Loading configuration from params.yaml
        config_path = os.path.join(os.path.dirname(__file__), 'config', 'params.yaml')
        with open(config_path, 'r') as file:
            config_params = yaml.safe_load(file)

        #Initializing wandb with the loaded configuration
        wandb.init(project="final_project", entity="mlops11", config=config_params)

        self.grid_search.fit(X_train)

        for i, score in enumerate(self.grid_search.cv_results_['mean_test_score']):
            wandb.log({
                "calmar_ratio": score
            })

        script_dir = os.path.dirname(os.path.realpath(__file__))
        project_dir = os.path.dirname(script_dir)
        summary_path = os.path.join(project_dir, 'reports', 'summary.csv')

        if os.path.exists(summary_path):
            summary_df = pd.read_csv(summary_path)
            summary_table = wandb.Table(dataframe=summary_df)    #Convert the pandas DataFrame into a wandb Table
            wandb.log({"summary": summary_table})    # Log the summary table to wandb
        else:
            print(f"Error: The file {summary_path} does not exist.")

        wandb.finish()

    def save_model(self, model_path, benchmark_path):
        with open(model_path, 'wb') as file:
            pickle.dump(self.model_stacking, file)
        with open(benchmark_path, 'wb') as file:
            pickle.dump(self.benchmark, file)

def main():
    # Initialize the model trainer
    trainer = ModelTrainer()

    # Tune the parameters
    trainer.tune_parameters()

    # Load the training data
    script_dir = os.path.dirname(__file__)
    processed_data_dir = os.path.join(script_dir, '../data/processed')
    X_train = pd.read_csv(os.path.join(processed_data_dir, 'X_train.csv'), index_col=0)

    # Train the model
    trainer.train(X_train)

    # Save the model
    model_dir = os.path.join(script_dir, '../models/')
    model_path = os.path.join(model_dir, 'model.pkl')
    benchmark_path = os.path.join(model_dir, 'benchmark.pkl')
    trainer.save_model(model_path, benchmark_path)

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.dump_stats('program.prof')  # Save the stats to a file
