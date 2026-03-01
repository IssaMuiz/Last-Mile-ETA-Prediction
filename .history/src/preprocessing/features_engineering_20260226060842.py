"""This module is responsible for features engineering"""
import numpy as np


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
        lat2 = np.radians(lat2)
        lon1 = np.radians(lon1)
        lon2 = np.radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arcsin(np.sqrt(a))

        return R * c

    except Exception as e:
        print(f"An error occured during Haversine distance calculation: {e}")
        raise
