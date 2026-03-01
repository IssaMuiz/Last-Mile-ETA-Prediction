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

        # Convert latitude and longitude from degrees to radians
        lat1 = np.radians(lat1)
        lon1 = np.radians(lon1)
        lat2 = np.radians(lat2)
        lon2 = np.radians(lon2)

        dlat = lat2 - lat1  # Calculate the differences in latitude and longitude
        dlon = lon2 - lon1

        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * \
            np.sin(dlon/2)**2  # Haversine formula
        c = 2 * np.arcsin(np.sqrt(a))  # Calculate the distance in kilometers

        return R * c  # Return the distance in kilometers

    except Exception as e:
        print(f"An error occured during Haversine distance calculation: {e}")
        raise


def add_new_features(df: pd.DataFrame):
    """Add a new features 'Distance', 'Order_hour', 'Order_dayofweek', and 'Is_weekend' to the dataframe by calculating the Haversine distance between the pickup and dropoff locations
    parameters:
    df (pd.DataFrame): The dataframe for the dataset
    Returns:
    pd.DataFrame: A Dataframe containing the new features added 

    """
    try:
        df['Distance_km'] = haversine_distance(
            # Calculate distance in kilometers
            df['Store_Latitude'], df['Store_Longitude'], df['Drop_Latitude'], df['Drop_Longitude'])

        # Extract hour of the day from Order_Time
        df['Order_hour'] = df['Order_Time'].dt.hour
        # Extract day of the week from Order_Time (0=Monday, 6=Sunday)
        df['Order_dayofweek'] = df['Order_Time'].dt.dayofweek
        # Create a binary feature indicating if the order was placed on a weekend (1 for weekend, 0 for weekday)
        df['Is_weekend'] = df['Order_dayofweek'].isin([5, 6]).astype(int)

        # Handle cases where Pickup_Time is earlier than Order_Time
        mask = df["Pickup_Time"] < df["Order_Time"]

        df.loc[mask, "Pickup_Time"] = (
            # Adjust Pickup_Time to the next day if it's earlier than Order_Time
            df.loc[mask, "Pickup_Time"] + pd.Timedelta(days=1))
        df['Prep_time_minutes'] = (
            # Calculate preparation time in minutes
            df['Pickup_Time'] - df['Order_Time']).dt.total_seconds() / 60.0
        print("New features added successfully")
        return df
    except Exception as e:
        print(f"An error occured during adding new features: {e}")
        raise


def drop_columns(df: pd.DataFrame, column_names: list[str]):
    """Drop specified columns from the dataframe
    parameters:
    df (pd.DataFrame): The dataframe for the dataset
    column_names: Column names to be dropped
    Returns: A Dataframe with specified columns dropped"""

    try:
        df = df.drop(column_names, axis=1)
        print(f"{', '.join(column_names)} columns dropped")
        return df

    except Exception as e:
        print(f"An error occured while dropping the specified columns: {e}")
        raise
