from sklearn.model_selection import train_test_split
from skfolio.datasets import load_ftse100_dataset
from skfolio.preprocessing import prices_to_returns
import numpy as np


prices = load_ftse100_dataset()
X = prices_to_returns(prices)
#X_train, X_test = train_test_split(X, test_size=0.50, shuffle=False)

print(type(X))
print(X.shape)
print(X)
print(X.columns)
