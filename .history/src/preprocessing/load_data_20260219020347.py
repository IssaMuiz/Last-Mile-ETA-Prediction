"""This module is responsible for loading data for the last-mile ETA prediction model. It includes functions for reading data from CSV files"""

import pandas as pd


def load_data(file_path):
    """Loads data from a CSV file and returns a pandas DataFrame."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None
