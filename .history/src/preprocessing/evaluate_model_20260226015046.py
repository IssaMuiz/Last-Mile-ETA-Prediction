"""This module is responsible for model evaluation"""
import pandas as pd
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score


def evaluate_model(model, X_val, y_val):
    """Evaluate the trained model on validation set

    parameters:
    model: The trained linear regression model
    X_val: The validation features
    y_val: The validation target variable

    Returns: 
    dict: A dictionary containing the evaluation metrics (MAE, RMSE, R2_SCORE)
    """
    try:
        y_pred = model.predict(X_val)

        mae = mean_absolute_error(y_val, y_pred)
        rmse = root_mean_squared_error(y_val, y_pred)
        R2 = r2_score(y_val, y_pred)
        print(f"Model evaluation completed successfully")
        return {"MAE": mae, "RMSE:": rmse, "R2_SCORE": R2}

    except Exception as e:
        print(f"An error occured during model evaluation: {e}")
        raise
