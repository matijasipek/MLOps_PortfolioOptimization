import sys
import os
sys.path.insert(1, os.path.join(os.path.dirname(__file__), '../src'))
from tests import _PATH_DATA
import pandas as pd
import pytest
from train_model import ModelTrainer
from models.model import Models
from sklearn.model_selection import GridSearchCV
from skfolio.model_selection import  WalkForward
import wandb


@pytest.fixture(autouse=True)
def setup_wandb():
    wandb.login(key="786d9a30ddbe8d6b543db95e7d0e64433c61c0c2")

def test_model_initialization():

    trainer = ModelTrainer()
    assert isinstance(trainer.models, Models)
    assert trainer.model_stacking is not None
    assert trainer.benchmark is not None

def test_parameter_tuning():
    trainer = ModelTrainer()
    trainer.tune_parameters()
    assert isinstance(trainer.cv, WalkForward)
    assert isinstance(trainer.grid_search, GridSearchCV)

def test_model_training():
    trainer = ModelTrainer()
    trainer.tune_parameters()
    X_train = pd.read_csv(_PATH_DATA + '/processed/X_train.csv', index_col=0)
    trainer.train(X_train)
    assert trainer.model_stacking is not None

def test_model_saving():
    script_dir = os.path.dirname(__file__)
    model_dir = os.path.join(script_dir, '../models/')
    model_path = os.path.join(model_dir, 'model.pkl')
    benchmark_path = os.path.join(model_dir, 'benchmark.pkl')

    trainer = ModelTrainer()
    trainer.save_model(model_path, benchmark_path)

    assert os.path.exists(model_path)
    assert os.path.exists(benchmark_path)