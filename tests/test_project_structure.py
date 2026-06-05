from wastewater_ml.config.model_registry import classifiers, regressors
from wastewater_ml.evaluation.validation import pred_check


def test_model_registry_has_expected_coverage():
    assert len(classifiers) >= 15
    assert len(regressors) >= 15
    assert classifiers["lgbm"] == "LightGBM Classifier"
    assert regressors["xgb"] == "XGBoost Regressor"


def test_predictor_validation_accepts_single_and_multi_model_inputs():
    assert pred_check("lr", pred_type="classification") == (True, "lr")
    assert pred_check(["lin", "rfr"], pred_type="regression") == (True, None)


def test_predictor_validation_rejects_unknown_model():
    assert pred_check("made_up_model", pred_type="classification") == (
        False,
        "made_up_model",
    )
