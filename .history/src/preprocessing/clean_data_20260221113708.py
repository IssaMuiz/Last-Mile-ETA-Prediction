"""This module is responsible for cleaning and fixing 
the data for the amazon last-mile eta dataset"""

import pandas as pd


def drop_column(df: pd.DataFrame, column_name: str):
    """
    drop unused column from the dataframe

    parameters:
    df (pd.DataFrame): The dataframe for the dataset
    column_name: The name of the column to be dropped
    Returns: pd.DataFrame: A dataframe with a specified column dropped
    """
    try:
        df = df.drop(column_name, axis=1)
        print(f"{column_name} column dropped successfully")
        return df
    except KeyError:
        print(f"Error: {column_name} column is not found in the dataframe")
        raise
    except Exception as e:
        print(f"An error occured during dropping column: {e}")
        raise


def date_conversion(df: pd.DataFrame):
    """
    convert date column from string format to datetime format

    parameters:
    df (pd.DataFrame): The dataframe for the 
    Returns: 
    pd.DataFrame: A Dataframe containing the converted column to datetime format
    """
    try:
        df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%Y-%m-%d")
        print("Order Date column converted to datetime format successfully")
        return df
    except KeyError:
        print(
            "Error: Order Date column is not found in the dataframe")
        raise
    except Exception as e:
        print(f"An error occured during datetime conversion: {e}")
        raise


def time_conversion(df: pd.DataFrame, columns: list[str]):
    """convert time column from string format to datetime format
    parameters:
    df (pd.DataFrame): The dataframe for the 
    columns (list[str]): The list of column names to be converted to datetime format
    Returns: 
    pd.DataFrame: A Dataframe containing the converted columns to datetime format
    """

    try:
        for column in columns:
            df[column] = pd.to_datetime(df[column].astype(
                str).str.strip(), format="%H:%M:%S").dt.time
            print("Time columns converted to datetime format successfully")
            return df
    except KeyError:
        print(f"Error: {column} is not found in the dataframe")
        raise
    except Exception as e:
        print(f"An error occured during datetime conversion: {e}")
        raise


def impute_missing_values_for_weather(df: pd.DataFrame, column_name: str, impute_value: str):
    """
    Impute missing values in the weather column with a specified value

    parameters:
    df (pd.DataFrame): The dataframe for the dataset
    column_name: The name of the column to be imputed
    impute_value: The value to be used for imputing missing values

    Returns: pd.DataFrame: A dataframe with missing values in the weather column imputed
    """

    try:
        df[column_name] = df[column_name].fillna(impute_value)
        print(f"Missing values in {column_name} column imputed successfully")
        return df
    except KeyError:
        print(f"Error: {column_name} column is not fouund in the dataset")
        raise
    except Exception as e:
        print(f"An error occured during imputation: {e}")
        raise


def impute_missing_values_for_agent_rating(df: pd.DataFrame):
    """Impute missing values in the agent rating column using median

    parameters: 
    df (pd.DataFrame): The dataframe for the dataset
    column_name: The name of the column to be imputed
    Returns: pd.DataFrame: A dataframe with missing values in the agent rating column imputed  
    """

    try:
        df['Agent_Rating_missing'] = df['Agent_Rating'].isna().astype(int)
        df['Agent_Rating'] = df['Agent_Rating'].fillna(
            df['Agent_Rating'].median())
        print("Missing values in Agent_Rating column flags and imputed successfully")
        return df
    except KeyError:
        print("Error: Agent_Rating column is not found in the dataset")
        raise
    except Exception as e:
        print(f"An error occured during imputation: {e}")
        raise


def drop_rows_with_missing_values(df: pd.DataFrame, column_name: str):
    """
    Drop a missing values in a specified column

    paramters: 
    df (pd.DataFrame): The dataframe for the dataset
    column_name: The name of the column to be checked for missing values and dropped
    Returns: pd.DataFrame: A dataframe with missing values in the specified column dropped

    """
    try:
        df = df.dropna(subset=[column_name])
        df = df.reset_index(drop=True)
        print("rows with missing values dropped successfully")
        return df
    except Exception as e:
        print(
            f"An error occured during dropping rows with missing values: {e}")
        raise
