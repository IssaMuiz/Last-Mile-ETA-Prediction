"""This module is responsible for cleaning and fixing 
the data for the amazon last-mile eta dataset"""

import pandas as pd


def date_conversion(df: pd.DataFrame):
    """
    convert date or time from string format to datetime format

    parameters:
    df (pd.DataFrame): The dataframe for the 
    columns (list[str]): The list of column names to be converted to datetime format
    Returns: 
    pd.DataFrame: A Dataframe containing the converted columns to datetime format
    """
    try:
        df["Order Date"] = pd.to_datetime(df["Order Date"], format="%Y-%m-%d")
        print(f"Order Date column converted to datetime format successfully")
        return df
    except KeyError:
        print(
            f"Error: Order Date column is not found in the dataframe")
        raise
    except Exception as e:
        print(f"An error occured during datetime conversion: {e}")
        raise
