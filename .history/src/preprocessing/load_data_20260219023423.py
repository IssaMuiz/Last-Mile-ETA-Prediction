"""This module is responsible for loading data for the last-mile ETA prediction model. 
It includes functions for reading data from CSV files"""

import pandas as pd
import sys


def load_data(file_path):
    """
    Load the Amazon last-mile eta data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the Amazon last-mile eta data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
        sys.exit(1)
    except (pd.errors.ParserError, ValueError) as e:
        print(f"An error occurred while loading the data: {e}")
        sys.exit(1)
