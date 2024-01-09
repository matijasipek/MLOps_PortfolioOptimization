from plotly.io import show
from sklearn.model_selection import train_test_split
from skfolio.preprocessing import prices_to_returns
import pandas as pd
import os


### DATA
# DATA
script_dir = os.path.dirname(__file__)  # get the directory of the current script
rel_path = '../../data/raw/ftse100_dataset.csv.gz'
abs_file_path = os.path.join(script_dir, rel_path)
prices_raw = pd.read_csv(abs_file_path)
prices_raw['Date'] = pd.to_datetime(prices_raw['Date'])
prices_raw = prices_raw.set_index('Date')

## PREPROCESSING
X = prices_to_returns(prices_raw)
print(type(prices_raw))
X_train, X_test = train_test_split(X, test_size=0.50, shuffle=False)

# Save Processed data
processed_data_dir = os.path.join(script_dir, '../../data/processed')
X_train.to_csv(os.path.join(processed_data_dir, 'X_train.csv'))
X_test.to_csv(os.path.join(processed_data_dir, 'X_test.csv'))

