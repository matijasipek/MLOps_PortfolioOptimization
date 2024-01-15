# Financial Portfolio Optimization Using skfolio

## Project Overview
This project leverages the open-source machine learning library `skfolio` to optimize financial portfolios using Stacking Optimization. 

### Key Objectives:
- Utilize `skfolio` for financial portfolio optimization.
- Implement Stacking Optimization as an ensemble method.
- Focus on the DevOps aspects of the project, with a simplified approach to model selection and hyperparameter tuning.

## Dataset
The project uses the FTSE 100 dataset, which includes daily prices of 64 assets from the FTSE 100 Index, spanning from 2000-01-04 to 2023-05-31.

## Implementation Details
- **Simplicity and Focus:** The project is designed with a focus on the DevOps part of the course. Therefore, models are used as-is, with only simple grid search tuning of hyperparameters.
- **Data Handling:** The FTSE 100 dataset is loaded and processed to fit the requirements of the stacking models. This is the given data set by the creators of the library

## Stacking Models
The stacking approach incorporates four different portfolio models:
1. Inverse Volatility
2. Maximum Diversification
3. Maximum Mean-Risk Utility allowing short position with L1 regularization
4. Hierarchical Equal Risk Contribution
-> In the end the stacking algorithm shows all model approaches in a graph and gives the best one.

## Reference
For more details on the stacking method implemented in `skfolio`, visit [Stacking Optimization Example in skfolio](https://skfolio.org/auto_examples/6_ensemble/plot_1_stacking.html#sphx-glr-auto-examples-6-ensemble-plot-1-stacking-py).
