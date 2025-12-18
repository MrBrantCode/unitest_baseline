"""
QUESTION:
Create a function named `top_3_polluted_bodies_of_water` that takes a list of dictionaries as input, where each dictionary represents a body of water with keys 'name', 'region', 'country', 'pollution_level', and 'population'. The function should return the names of the top 3 bodies of water with the most severe water pollution, prioritizing bodies of water with high pollution but low population over bodies of water with lower pollution but higher population. The 'pollution_level' is a number between 0 and 1, and a higher value indicates more severe pollution.
"""

def top_3_polluted_bodies_of_water(data):
    """
    Returns the names of the top 3 bodies of water with the most severe water pollution,
    taking into account the population living in the vicinity of the body of water.
    """
    sorted_data = sorted(data, key=lambda x: (x['pollution_level'], -x['population']), reverse=True)
    return [d['name'] for d in sorted_data[:3]]