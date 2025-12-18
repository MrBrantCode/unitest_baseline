"""
QUESTION:
Create a function `filter_odd_countries` that takes a list of country names as input and returns a new list containing only the country names with an odd number of letters in their names, without using loops or iteration.
"""

def filter_odd_countries(country_names):
    """
    This function takes a list of country names and returns a new list containing only the country names with an odd number of letters in their names.
    
    Args:
        country_names (list): A list of country names.
    
    Returns:
        list: A new list containing only the country names with an odd number of letters in their names.
    """
    return [country for country in country_names if len(country) % 2 == 1]