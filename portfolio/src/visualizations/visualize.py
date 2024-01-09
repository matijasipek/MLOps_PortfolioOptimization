
### PREDICT MODEL
pred_bench = cross_val_predict(
    benchmark,
    X_test,
    cv=cv,
    portfolio_params=dict(name="Benchmark"),
)

pred_stacking = cross_val_predict(
    model_stacking,
    X_test,
    cv=cv,
    n_jobs=-1,
    portfolio_params=dict(name="Stacking"),
)