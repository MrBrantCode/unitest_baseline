"""
QUESTION:
Write a function named quantum_realities that calculates and returns the number of possible realities given the number of quantum events and the average outcomes per event. The function should take two parameters: num_events and avg_outcomes.
"""

def quantum_realities(num_events, avg_outcomes):
    """
    Calculate the number of possible realities given the number of quantum events and the average outcomes per event.

    Parameters:
    num_events (int): The number of quantum events.
    avg_outcomes (int): The average outcomes per event.

    Returns:
    int: The number of possible realities.
    """
    return avg_outcomes ** num_events