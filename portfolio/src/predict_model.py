import torch
import dill as pickle
import os
from skfolio import Population

from skfolio.model_selection import (
    cross_val_predict,
    WalkForward,
)


def predict(data_file) -> None:   
    ### 
    # model location
    script_dir = os.path.dirname(__file__)  # get the directory of the current script
    model_dir = os.path.join(script_dir, '../models/')# Define the path to save the model file
    model_path = os.path.join(model_dir, 'model.pkl')
    # new data location
    predict_data = os.path.join(script_dir, '../data/processes/', data_file)
    # reports
    figures_dir = os.path.join(script_dir, '../reports/figures')
    reports_dir = os.path.join(script_dir, '../reports')
        

    # load a pre-trained model
    with open(model_path, 'rb') as file:
        loaded_model = pickle.load(file)
    print(f"Model read from {model_path}")
    

    cv = WalkForward(train_size=252, test_size=60)
    pred_stacking = cross_val_predict(
        loaded_model,
        predict_data,
        cv=cv,
        n_jobs=-1,
        portfolio_params=dict(name="Stacking"),
    )

    population = Population([pred_stacking])
    fig1 = population.plot_cumulative_returns()
    fig1.show()
    return None

if __name__ == "__main__": 
    predict('X_test.csv')