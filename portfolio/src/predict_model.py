import torch
import dill as pickle
import os
from skfolio import Population
import pandas as pd

from skfolio.model_selection import (
    cross_val_predict,
    WalkForward,
)

# Plotly 
from plotly.io import write_image
import plotly.express as px



def predict(data_file) -> None:   
    # model location
    script_dir = os.path.dirname(__file__)  # get the directory of the current script
    model_dir = os.path.join(script_dir, '../models/')# Define the path to save the model file
    model_path = os.path.join(model_dir, 'model.pkl')
    # new data location
    predict_data = os.path.join(script_dir, '../data/processed/', data_file)
    # reports
    figures_dir = os.path.join(script_dir, '../reports/figures')
    reports_dir = os.path.join(script_dir, '../reports')
        
    # load a pre-trained model
    with open(model_path, 'rb') as file:
        loaded_model = pickle.load(file)
    # data for prediction
    X_test = pd.read_csv(predict_data, index_col=0)

    print(predict_data)
    cv = WalkForward(train_size=252, test_size=60)
    pred_stacking = cross_val_predict(
        loaded_model,
        X_test,
        cv=cv,
        n_jobs=-1,
        portfolio_params=dict(name="Stacking"),
    )

    population = Population([pred_stacking])
    fig1 = population.plot_cumulative_returns()
    fig2 = population.plot_composition(display_sub_ptf_name=False)
    fig1.write_json(os.path.join(figures_dir, 'plot_cumulative_returns.json'))
    fig2.write_json(os.path.join(figures_dir, 'plot_composition.json'))

    # Create an empty list to store the data
    data = []

    # Loop through the population
    for ptf in population:
        print(f"Sharpe ratio : {ptf.annualized_sharpe_ratio:0.2f}")
        print(f"CVaR ratio : {ptf.cdar_ratio:0.5f}")
        print(f"Calmar ratio : {ptf.calmar_ratio:0.5f}")
        print("\n")

        # Append the data to the list
        data.append({
            'Sharpe Ratio': ptf.annualized_sharpe_ratio,
            'CVaR Ratio': ptf.cdar_ratio,
            'Calmar Ratio': ptf.calmar_ratio
        })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(reports_dir, 'report.csv'), index=False)
    summary = population.summary()
    summary.to_csv(os.path.join(reports_dir, 'summary.csv'), index=False)
    
    return None

if __name__ == "__main__": 
    predict('X_test.csv')