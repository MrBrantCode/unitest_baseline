"""
QUESTION:
Create a function named `transform_to_nested_dict` that takes a list of lists as input, where each sublist contains a string representing a country name, an integer representing the population, and a list of three strings representing nominal GDP, GDP (PPP), and GDP per capita respectively. The function should return a nested dictionary where each country name is a key, and its corresponding value is another dictionary containing the population and GDP data.
"""

def transform_to_nested_dict(data_list):
    dictionary = {}
    for item in data_list:
        country_name, population, gdp_data = item
        dictionary[country_name] = {"Population": population, "GDP": {"Nominal GDP": gdp_data[0], "GDP (PPP)": gdp_data[1], "GDP per Capita": gdp_data[2]}}
    return dictionary