"""This module is for model training"""
from sklearn.linear_model import LinearRegression
from src.preprocessing.evaluate_model import evaluate_model


def build_model():
    """Intantiate the linear model"""
    try:
        model = LinearRegression()
        return model
    except Exception as e:
        print(f"An errror occured during model building: {e}")
        raise


def train_model(model, X_train, y_train):
    """Train the linear model  
    parameters:
    model: The linear regression model
    X_train: The training features
    y_train: The training target variable

    Returns:
    model: The trained linear regression model

    """
    try:
        model.fit(X_train, y_train)
        print("Model trained successfully")
        return model
    except Exception as e:
        print(f"An error occured during model training: {e}")
        raise


def run_model(X_train, y_train, X_val, y_val):
    """Run the model training and evaluation pipeline
    parameters:
    X_train: The training features
    y_train: The training target variable
    X_val: The validation features
    y_val: The validation target variable

    Returns:
    dict: A dictionary containing the evaluation metrics (MAE, RMSE, R2_SCORE)

    """
    try:

        model = build_model()
        train = train_model(model, X_train, y_train)

        evaluation_metrics = evaluate_model(train, X_val, y_val)

        return evaluation_metrics

    except Exception as e:
        print(f"An error occured during model training and evaluation: {e}")
        raise
