"""
QUESTION:
Create a function called `build_city_temperatures` that takes a list of month names and a list of corresponding average high temperatures in Celsius as input. The function should return a dictionary where the keys are the month names and the values are the average high temperatures. The months and temperatures should be paired by their order in the input lists.
"""

def build_city_temperatures(months, temperatures):
    """
    This function takes a list of month names and a list of corresponding average high temperatures 
    in Celsius as input, and returns a dictionary where the keys are the month names and the values 
    are the average high temperatures.

    Args:
    months (list): A list of month names.
    temperatures (list): A list of corresponding average high temperatures in Celsius.

    Returns:
    dict: A dictionary where the keys are the month names and the values are the average high temperatures.
    """
    return dict(zip(months, temperatures))