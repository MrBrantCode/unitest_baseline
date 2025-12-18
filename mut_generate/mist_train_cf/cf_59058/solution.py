"""
QUESTION:
Propose a synthetic attribute that can enhance the precision of a regression analysis model for predicting house prices. The attribute should incorporate location-based information and consider factors such as distance to public transportation, schools, supermarkets, hospitals, and parks. The goal is to improve the model's ability to account for location convenience and its impact on house prices.
"""

def calculate_proximity_to_amenities_score(distance_to_public_transportation, 
                                           distance_to_schools, 
                                           distance_to_supermarkets, 
                                           distance_to_hospitals, 
                                           distance_to_parks):
    """
    Calculate a proximity to amenities score based on the distance to various amenities.

    Args:
        distance_to_public_transportation (float): Distance to the nearest public transportation in kilometers.
        distance_to_schools (float): Distance to the nearest school in kilometers.
        distance_to_supermarkets (float): Distance to the nearest supermarket in kilometers.
        distance_to_hospitals (float): Distance to the nearest hospital in kilometers.
        distance_to_parks (float): Distance to the nearest park in kilometers.

    Returns:
        float: Proximity to amenities score.
    """
    # Assign weights to each type of amenity (adjust these weights according to your specific needs)
    weights = {
        'public_transportation': 0.3,
        'schools': 0.2,
        'supermarkets': 0.2,
        'hospitals': 0.15,
        'parks': 0.15
    }

    # Calculate the proximity score for each amenity
    proximity_scores = {
        'public_transportation': 1 / (1 + distance_to_public_transportation),
        'schools': 1 / (1 + distance_to_schools),
        'supermarkets': 1 / (1 + distance_to_supermarkets),
        'hospitals': 1 / (1 + distance_to_hospitals),
        'parks': 1 / (1 + distance_to_parks)
    }

    # Calculate the weighted sum of proximity scores
    proximity_to_amenities_score = sum(weights[amenity] * proximity_scores[amenity] for amenity in weights)

    return proximity_to_amenities_score