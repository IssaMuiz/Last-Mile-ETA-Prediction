"""Splitting of data into training, testing and validation set"""
import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(df: pd.DataFrame, test_size=0.3, random_state=42):
    """Split the data into training and testing sets

    parameters:
    df (pd.DataFrame): The dataframe for the dataset
    test_size (float): The proportion of the dataset to include in the test split\
    random_state (int): The seed used by the random number generator

    Returns: 
    tuple: A tuple containing the training and testing sets (train, test, val)
    """

    try:
        train, test = train_test_split(df, test_size, random_state)
        val, test = train_test_split(test, test_size=0.5, random_state=42)
        print("Data splitted into training, testing and validation sets successfully")
        return train, test, val
    except Exception as e:
        print(f"An error occured during data splitting: {e}")
        raise


def split_features(df: pd.DataFrame):
    """Split the data into features and target variable

    parameters:
    df (pd.DataFrame): The dataframe for the dataset
    Returns:
    tuple: A tuple containing the features and target variable (X, y)
    """
    try:
        X = df.drop("Delivery_Time", axis=1)
        y = df["Delivery_Time"]
        print("Data splitted into features and target variable successfully")
        return X, y
    except Exception as e:
        print(
            f"An error occured during splitting features and target variable: {e}")
        raise
