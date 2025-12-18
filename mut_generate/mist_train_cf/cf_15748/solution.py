"""
QUESTION:
Create a dictionary of Indian states sorted in alphabetical order where each state is a key with a value of a list of its top 5 major cities. Each city is a dictionary containing 'name', 'population', 'area', and 'official_language'. The cities within a state should be sorted in descending order of population. Create a function `calculate_total_population(state)` that calculates the total population of all the cities in a given state.
"""

def calculate_total_population(state, states):
    """
    Calculate the total population of all the cities in a given state.

    Args:
    state (str): The name of the state.
    states (dict): A dictionary of Indian states where each state is a key with a value of a list of its top 5 major cities.

    Returns:
    int: The total population of all the cities in the given state.
    """
    total_population = 0
    for city in states[state]:
        total_population += city['population']
    return total_population