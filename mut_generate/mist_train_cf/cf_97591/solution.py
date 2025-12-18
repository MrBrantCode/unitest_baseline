"""
QUESTION:
Create a function named `top_3_polluted_bodies_of_water` that takes a list of dictionaries as input, where each dictionary contains the following keys: "name", "region", "country", "pollution_level", and "population". The function should return a list of the names of the top 3 bodies of water with the most severe water pollution, prioritizing bodies of water with high pollution levels and low population over those with lower pollution levels and higher population.
"""

def top_3_polluted_bodies_of_water(data):
    """
    Returns the names of the top 3 bodies of water with the most severe water pollution,
    taking into account the population living in the vicinity of the body of water.
    """
    sorted_data = sorted(data, key=lambda x: (x['pollution_level'], -x['population']), reverse=True)
    return [d['name'] for d in sorted_data[:3]]