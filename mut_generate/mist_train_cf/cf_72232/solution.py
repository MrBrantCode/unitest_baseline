"""
QUESTION:
Design a function `get_recommended_restaurants` that takes in a user's current location and their dietary preferences, and returns a list of recommended restaurants based on their past search history. The function should filter the recommendations based on the user's location and dietary preferences. Assume that the user's past search history and dietary preferences are stored in a database, and that a list of all restaurants with their locations, ratings, and cuisines is available.
"""

def get_recommended_restaurants(current_location, dietary_preferences, user_search_history, restaurants):
    """
    Returns a list of recommended restaurants based on the user's past search history, 
    current location, and dietary preferences.

    Parameters:
    current_location (str): The user's current location.
    dietary_preferences (list): A list of the user's dietary preferences (e.g. vegan, vegetarian, gluten-free).
    user_search_history (list): A list of the user's past search history.
    restaurants (list): A list of all restaurants with their locations, ratings, and cuisines.

    Returns:
    list: A list of recommended restaurants.
    """
    # Filter restaurants based on user's location
    nearby_restaurants = [restaurant for restaurant in restaurants if restaurant['location'] == current_location]

    # Filter restaurants based on user's dietary preferences
    suitable_restaurants = [restaurant for restaurant in nearby_restaurants 
                            for preference in dietary_preferences 
                            if preference in restaurant['cuisine']]

    # Filter restaurants based on user's past search history
    recommended_restaurants = [restaurant for restaurant in suitable_restaurants 
                               if restaurant['name'] in user_search_history]

    return recommended_restaurants