"""
QUESTION:
Write a function `country_info_to_nested_dict` that takes a list of country information as input. The list contains sublists, where each sublist is in the format [country_name, continent, population, languages]. The function should return a nested dictionary where the top-level keys are the continents, the second-level keys are the country names, and the values are dictionaries containing the population and a list of official languages for each country.
"""

def country_info_to_nested_dict(country_info_list):
    """
    This function transforms a list of country information into a nested dictionary.
    
    Args:
        country_info_list (list): A list of sublists containing country information.
            Each sublist is in the format [country_name, continent, population, languages].
    
    Returns:
        dict: A nested dictionary where the top-level keys are the continents, 
            the second-level keys are the country names, and the values are dictionaries 
            containing the population and a list of official languages for each country.
    """
    nested_dict = {}
    for country in country_info_list:
        continent = country[1]
        country_name = country[0]
        population = country[2]
        languages = country[3]
        
        if continent not in nested_dict:
            nested_dict[continent] = {}
            
        nested_dict[continent][country_name] = {"Population": population, "Languages": languages}
    
    return nested_dict