import torch
import time
import dill as pickle
import os
from skfolio import Population
import pandas as pd
import argparse
from prometheus_client import start_http_server, Counter, Summary, Gauge

from skfolio.model_selection import (
    cross_val_predict,
    WalkForward,
)

# Define custom metrics
PREDICTION_COUNT = Counter('prediction_count', 'Total number of predictions made')
PREDICTION_ERRORS = Counter('prediction_errors', 'Total number of prediction errors')
PREDICTION_LATENCY = Summary('prediction_latency_seconds', 'Time spent making predictions')
MODEL_LOAD_TIME = Gauge('model_load_time_seconds', 'Time taken to load the model into memory')


def predict(predict_data) -> None:
    prediction_start_time = time.time()   
   
    # Check if running inside a Docker container
    if os.environ.get('RUNNING_IN_DOCKER'):
        model_path = '/models/model.pkl'
        figures_dir = '/reports/figures'
        reports_dir = '/reports'
    else:
        script_dir = os.path.dirname(__file__)
        model_dir = os.path.join(script_dir, '../models/')
        model_path = os.path.join(model_dir, 'model.pkl')
        figures_dir = os.path.join(script_dir, '../reports/figures')
        reports_dir = os.path.join(script_dir, '../reports')

    # load a pre-trained model
    model_load_start_time = time.time()
    with open(model_path, 'rb') as file:
        loaded_model = pickle.load(file)
    MODEL_LOAD_TIME.set(time.time() - model_load_start_time)

    population = None  # Initialize population variable
    
    try:
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
    except Exception as e:
        PREDICTION_ERRORS.inc()
        raise e
    finally:
        # Record the latency metric
        PREDICTION_LATENCY.observe(time.time() - prediction_start_time)

    if population is not None:
        PREDICTION_COUNT.inc()

    df = pd.DataFrame(data)
    df.to_csv(os.path.join(reports_dir, 'report.csv'), index=False)
    summary = population.summary()
    summary.to_csv(os.path.join(reports_dir, 'summary.csv'), index=False)
    
    return None

if __name__ == "__main__":
    # Start the Prometheus metrics server
    start_http_server(8000)

    parser = argparse.ArgumentParser(description='Predict data.')
    parser.add_argument('data_file', type=str, help='The path to the data file.')
    args = parser.parse_args()
    predict(args.data_file)

    # Keep the server running
    while True:
        time.sleep(1)