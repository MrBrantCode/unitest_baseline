"""
QUESTION:
Create a function `convert_to_nested_dict` that takes a list of lists as input, where each sublist contains a country name, a continent name, and a population. The function should return a nested dictionary where the top-level keys are the continent names, and the values are dictionaries with the country names as keys and their populations as values.
"""

def convert_to_nested_dict(country_data):
    """
    This function converts a list of country data into a nested dictionary.
    
    Args:
    country_data (list): A list of lists, where each sublist contains a country name, 
                         a continent name, and a population.
    
    Returns:
    dict: A nested dictionary where the top-level keys are the continent names, and 
          the values are dictionaries with the country names as keys and their 
          populations as values.
    """
    
    result = {}
    
    for item in country_data:
        country = item[0]
        continent = item[1]
        population = item[2]
        
        if continent not in result:
            result[continent] = {}
        
        result[continent][country] = population
    
    return result