"""
QUESTION:
Implement a function `build_city_hierarchy(city_parent_dict, city_names)` that takes two dictionaries as input: `city_parent_dict` where the keys are the city codes and the values are the province codes to which the cities belong, and `city_names` where the keys are the city codes and the values are the names of the cities. The function should return a nested dictionary representing the hierarchical structure of the cities within their respective parent provinces, where the top-level keys are the unique province codes and the value for each province code key is another dictionary representing the cities within that province.
"""

def build_city_hierarchy(city_parent_dict, city_names):
    """
    This function builds a nested dictionary representing the hierarchical structure of cities within their respective parent provinces.

    Args:
        city_parent_dict (dict): A dictionary where the keys are the city codes and the values are the province codes to which the cities belong.
        city_names (dict): A dictionary where the keys are the city codes and the values are the names of the cities.

    Returns:
        dict: A nested dictionary representing the hierarchical structure of the cities within their respective parent provinces.
    """

    city_hierarchy = {}
    
    for city, province in city_parent_dict.items():
        if province in city_hierarchy:
            city_hierarchy[province][city] = city_names[city]
        else:
            city_hierarchy[province] = {city: city_names[city]}
    
    return city_hierarchy