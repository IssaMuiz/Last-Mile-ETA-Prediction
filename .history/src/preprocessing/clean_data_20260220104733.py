"""This module is responsible for cleaning and fixing the data for the amazon last-mile eta dataset"""

import pandas as pd


def datetime_conversion(df: pd.DataFrame, columns: list[str]):
    """
    convert date or time from string format to datetime format

    parameters:
    df (pd.DataFrame): The dataframe for the 

    Returns: 
    pd.DataFrame: A Dataframe containing the converted columns to datetime format
    """
    try:
        df[columns] = pd.to_datetime(df[columns])
        print(f"{columns} columns converted to datetime format successfully")
        return df
    except KeyError:
        print(f"Error: {columns} columns is not found in the dataframe")
        raise
    except Exception as e:
        print(f"An error occured during datetime conversion: {e}")
        raise
