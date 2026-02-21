"""This module is responsible for cleaning and fixing 
the data for the amazon last-mile eta dataset"""

import pandas as pd


def datetime_conversion(df: pd.DataFrame, column: str):
    """
    convert date or time from string format to datetime format

    parameters:
    df (pd.DataFrame): The dataframe for the 
    columns (list[str]): The list of column names to be converted to datetime format
    Returns: 
    pd.DataFrame: A Dataframe containing the converted columns to datetime format
    """
    try:
        df[column] = pd.to_datetime(df[column], format="%Y-%m-%d")
        print(f"{column} column converted to datetime format successfully")
        return df
    except KeyError:
        print(f"Error: {column} column is not found in the dataframe")
        raise
    except Exception as e:
        print(f"An error occured during datetime conversion: {e}")
        raise
