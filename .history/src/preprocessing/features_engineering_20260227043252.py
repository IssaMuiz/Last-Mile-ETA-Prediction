"""This module is responsible for features engineering"""
import numpy as np
import pandas as pd


def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate the Haversine distance between two points on the Earth specified in decimal degrees
    parameters:
    lat1, lon1: Latitude and Longitude of the first point
    lat2, lon2: Latitude and Longitude of the second point
    Returns:
    float: The Haversine distance in kilometers
    """
    try:
        R = 6371.0  # Radius of the Earth in kilometers

        lat1 = np.radians(lat1)
        lon1 = np.radians(lon1)
        lat2 = np.radians(lat2)
        lon2 = np.radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arcsin(np.sqrt(a))

        return R * c

    except Exception as e:
        print(f"An error occured during Haversine distance calculation: {e}")
        raise


def add_distance_feature(df: pd.DataFrame):
    """Add a new feature 'Distance' to the dataframe by calculating the Haversine distance between the pickup and dropoff locations
    parameters:
    df (pd.DataFrame): The dataframe for the dataset
    Returns:
    pd.DataFrame: The dataframe with the new 'Distance' feature

    """
    try:
        df['Distance_km'] = haversine_distance(
            df['Store_Latitude'], df['Store_Longitude'], df['Drop_Latitude'], df['Drop_Longitude'])

        print("Distance feature added successfully")

        df['Order_hour'] = df['Order_Time'].dt.hour
        df['Order_dayofweek'] = df['Order_Time'].dt.dayofweek
        return df
    except Exception as e:
        print(f"An error occured during adding distance feature: {e}")
        raise
