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


X = prices_to_returns(prices_raw)
print(type(prices_raw))
X_train, X_test = train_test_split(X, test_size=0.50, shuffle=False)

# Processed data
processed_data_dir = os.path.join(script_dir, '../../data/processed')
X_train.to_csv(os.path.join(processed_data_dir, 'X_train.csv'))
X_test.to_csv(os.path.join(processed_data_dir, 'X_test.csv'))


#

# ### PREDICTION
# pred_bench = cross_val_predict(
#     benchmark,
#     X_test,
#     cv=cv,
#     portfolio_params=dict(name="Benchmark"),
# )

# pred_stacking = cross_val_predict(
#     model_stacking,
#     X_test,
#     cv=cv,
#     n_jobs=-1,
#     portfolio_params=dict(name="Stacking"),
# )

# print("pred_bench", pred_bench)
# print("pred_stacking", pred_stacking)


# ### POPULATION ANALYSIS
# population = Population([pred_bench, pred_stacking])

# # Plot cumulative returns and save the figure
# fig1 = population.plot_cumulative_returns()pip install "dvc[gs]"pip install "dvc[gs]"
# fig1.show()