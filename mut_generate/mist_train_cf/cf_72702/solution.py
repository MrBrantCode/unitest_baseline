"""
QUESTION:
Create a function named `create_location_dict` that returns a dictionary containing a key named "location" with a tuple value representing coordinates in the form of latitude and longitude.
"""

def create_location_dict(latitude, longitude):
    """
    Creates a dictionary with a key named "location" and a tuple value of latitude and longitude.

    Args:
        latitude (float): The latitude coordinate.
        longitude (float): The longitude coordinate.

    Returns:
        dict: A dictionary containing the location coordinates.
    """
    return {"location": (latitude, longitude)}