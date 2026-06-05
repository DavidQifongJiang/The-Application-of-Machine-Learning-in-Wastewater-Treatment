"""Minimal example of the reusable package API.

This script assumes you have already loaded a feature matrix and target series
from one of the project datasets.
"""

import pandas as pd

from wastewater_ml.pipelines.wudi_regression import Regression


features = pd.DataFrame(
    {
        "influent_cod": [120.0, 98.0, 130.0, 105.0],
        "temperature": [22.5, 21.0, 24.1, 20.8],
    }
)
target = pd.Series([0.82, 0.76, 0.88, 0.79])

model = Regression(predictor=["lin"], cv_folds=2, test_size=0.25)
model.fit(features, target)
print(model.result())
