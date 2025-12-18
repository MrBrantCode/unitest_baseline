"""
QUESTION:
Create a function `top_3_polluted_bodies_of_water` that takes in a list of dictionaries, where each dictionary represents a body of water with fields "name", "region", "country", "pollution_level" (between 0 and 1), and "population". The function should return the names of the top 3 bodies of water with the most severe water pollution, prioritizing bodies with high pollution but low population over those with lower pollution but higher population.
"""

def top_3_polluted_bodies_of_water(data):
    """
    Returns the names of the top 3 bodies of water with the most severe water pollution,
    taking into account the population living in the vicinity of the body of water.
    """
    sorted_data = sorted(data, key=lambda x: (x['pollution_level'], -x['population']), reverse=True)
    return [d['name'] for d in sorted_data[:3]]