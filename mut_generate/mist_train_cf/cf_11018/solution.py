"""
QUESTION:
Create a function `create_population_dict` that takes a list of country-population pairs as input and returns a dictionary where the keys are the country names and the values are the corresponding population counts. The function should be able to handle a list of any length.
"""

def create_population_dict(country_populations):
    """
    This function takes a list of country-population pairs as input and returns a dictionary 
    where the keys are the country names and the values are the corresponding population counts.

    Args:
        country_populations (list): A list of tuples containing country names and population counts.

    Returns:
        dict: A dictionary with country names as keys and population counts as values.
    """
    return dict(country_populations)