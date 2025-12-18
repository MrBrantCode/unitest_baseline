"""
QUESTION:
Create a function `create_ar_treasure_hunt` that designs a mobile app for an augmented reality treasure hunt inside a digital heritage site, utilizing augmented reality and geolocation features. The function should integrate the following elements: AR features, 3D models of game objects, and geolocation to guide players towards the physical location of treasures. The function should also include a user interface with a map to show the user's current location, track progress, and list of found treasures.
"""

def create_ar_treasure_hunt(site_layout, treasures, game_objects, user_location):
    """
    Designs a mobile app for an augmented reality treasure hunt inside a digital heritage site.

    Args:
        site_layout (dict): A dictionary containing the layout of the digital heritage site.
        treasures (list): A list of treasures to be hidden in the site.
        game_objects (list): A list of 3D models of game objects.
        user_location (tuple): The current location of the user.

    Returns:
        dict: A dictionary containing the AR features, geolocation data, and user interface.
    """
    
    # Initialize an empty dictionary to store the AR features, geolocation data, and user interface
    ar_treasure_hunt = {}
    
    # Define the AR features
    ar_features = {
        'treasures': treasures,
        'game_objects': game_objects
    }
    
    # Add the AR features to the ar_treasure_hunt dictionary
    ar_treasure_hunt['ar_features'] = ar_features
    
    # Define the geolocation data
    geolocation_data = {
        'site_layout': site_layout,
        'user_location': user_location
    }
    
    # Add the geolocation data to the ar_treasure_hunt dictionary
    ar_treasure_hunt['geolocation_data'] = geolocation_data
    
    # Define the user interface
    user_interface = {
        'map': site_layout,
        'progress': [],
        'found_treasures': []
    }
    
    # Add the user interface to the ar_treasure_hunt dictionary
    ar_treasure_hunt['user_interface'] = user_interface
    
    # Return the ar_treasure_hunt dictionary
    return ar_treasure_hunt