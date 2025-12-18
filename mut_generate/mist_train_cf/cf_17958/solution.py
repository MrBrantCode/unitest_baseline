"""
QUESTION:
Write a function `geocode_address` that takes a string `address` as input and returns a tuple containing the latitude and longitude. The address string is in the format "street address, city, state" and the function should use only primitive data types and not rely on any external libraries or APIs for geocoding. The latitude and longitude should be calculated based on the lengths of the street address and city names and a known location. 

Note: The solution should use approximations and assumptions and should not be used for accurate geocoding.
"""

def geocode_address(address):
    """
    Calculate the latitude and longitude of an address.

    Args:
        address (str): A string representing the address in the format "street address, city, state".

    Returns:
        tuple: A tuple containing the latitude and longitude of the address.
    """
    # Split the address into its components
    components = address.split(", ")
    street_address = components[0]
    city = components[1]
    state = components[2]

    # Calculate the latitude and longitude offsets
    latitude_offset = len(street_address) * 0.001
    longitude_offset = len(city) * 0.001

    # Use a known location as the base coordinates
    base_latitude = 37.7749
    base_longitude = -122.4194

    # Calculate the latitude and longitude of the address
    latitude = base_latitude + latitude_offset
    longitude = base_longitude + longitude_offset

    return (latitude, longitude)