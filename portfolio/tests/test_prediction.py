import os
import sys
sys.path.insert(1, os.path.join(os.path.dirname(__file__), '../src'))
import pandas as pd
import pytest
from src.predict_model import predict
import numpy as np
from tests import _PATH_DATA


def test_predict():
    # Define the path to the CSV file
    csv_file_path = os.path.join(_PATH_DATA+'/processed/', "X_test.csv")

    # Call the predict function
    predict(csv_file_path)

    # Check that the output files were created
    script_dir = os.path.dirname(__file__)
    figures_dir = os.path.join(script_dir, '../visualizations/figures')
    visualizations_dir = os.path.join(script_dir, '../visualizations')
    assert os.path.exists(os.path.join(figures_dir, 'plot_cumulative_returns.json'))
    assert os.path.exists(os.path.join(figures_dir, 'plot_composition.json'))
    assert os.path.exists(os.path.join(visualizations_dir, 'report.csv'))
    assert os.path.exists(os.path.join(visualizations_dir, 'summary.csv'))