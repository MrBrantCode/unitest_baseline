"""
QUESTION:
Create a function to display a table of cities, with columns for 'Name', 'Population', and 'Country'. The function should take a list of city objects as input, where each city object contains 'id', 'name', 'population', and 'country' properties. The function should return a table structure.
"""

def display_city_table(cities):
    """
    This function displays a table of cities with columns for 'Name', 'Population', and 'Country'.
    
    Args:
    cities (list): A list of city objects containing 'id', 'name', 'population', and 'country' properties.
    
    Returns:
    str: A table structure representing the cities data.
    """
    table = "<table><thead><tr><th>Name</th><th>Population</th><th>Country</th></tr></thead><tbody>"
    for city in cities:
        table += f"<tr><td>{city['name']}</td><td>{city['population']}</td><td>{city['country']}</td></tr>"
    table += "</tbody></table>"
    return table