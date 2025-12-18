"""
QUESTION:
Create a function `calculate_total_population` that takes a dictionary `states` where each key is an Indian state and its corresponding value is a list of its top 5 major cities. Each city is represented as a dictionary containing its name, population, area, and official language. The function should calculate and return the total population of all the cities in the given state. The dictionary should be sorted in alphabetical order by state and each city list should be sorted in descending order by population.
"""

def calculate_total_population(states, state):
    """
    Calculate the total population of all the cities in a given state.

    Args:
        states (dict): A dictionary containing Indian states as keys and a list of their top 5 major cities as values.
        state (str): The name of the state for which the total population needs to be calculated.

    Returns:
        int: The total population of all the cities in the given state.
    """
    total_population = 0
    for city in states.get(state, []):
        total_population += city['population']
    return total_population