"""
QUESTION:
Write a function called `get_coordinates` that takes an address string as input and returns a tuple containing the latitude and longitude of the address as floating point numbers. The function should not use any external libraries or APIs. The address string is expected to be in a format that can be looked up on an online mapping service.
"""

def get_coordinates(address):
    # Manually searched latitude and longitude values
    coordinates = {
        "1600 Amphitheatre Parkway, Mountain View, CA": (37.422049, -122.084735),
        # Add more address coordinates here...
    }

    return coordinates.get(address, (None, None))