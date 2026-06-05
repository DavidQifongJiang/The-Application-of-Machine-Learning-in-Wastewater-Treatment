# Model Card

## Problem

Predict and analyze wastewater treatment behavior from plant measurements and microbiome-derived features. The repository supports both:

- classification workflows for microbiome/treatment categories
- regression workflows for continuous treatment-efficiency/change-rate targets

## Model families

The package exposes a broad model registry:

- linear models: logistic regression, ridge, SGD, elastic net, Bayesian ridge
- tree ensembles: random forest, extra trees, gradient boosting, AdaBoost, bagging
- boosted trees: LightGBM, XGBoost, CatBoost
- distance/kernel models: KNN, SVM/SVR, kernel ridge
- neural baseline: multilayer perceptron

## Evaluation

The pipelines use train/validation splits plus K-fold cross-validation. Regression reports R2, MAE, RMSE, and K-fold R2. Classification reports validation accuracy and K-fold accuracy. Optional Optuna tuning searches model-specific hyperparameter spaces.

## Limitations

- The codebase preserves a research-notebook origin, so some notebooks may contain stale exploratory cells.
- Notebook outputs should be treated as experimental records, not a fully locked benchmark suite.
- Production use would need stricter dataset versioning, leakage checks, and pinned dependency versions.
