"""
QUESTION:
Create a function called `sorted_city_temperatures` that builds a dictionary containing the names of the months as keys and tuples of the average high and low temperatures as values. The dictionary must be sorted in ascending order based on the average high temperatures. The input data will be a dictionary where the keys are the names of the months and the values are tuples of the average high and low temperatures.
"""

def sorted_city_temperatures(city_temperatures):
    """
    Builds a dictionary containing the names of the months as keys and tuples of 
    the average high and low temperatures as values, sorted in ascending order 
    based on the average high temperatures.

    Args:
        city_temperatures (dict): A dictionary where the keys are the names of 
            the months and the values are tuples of the average high and low 
            temperatures.

    Returns:
        dict: A dictionary containing the names of the months as keys and tuples 
            of the average high and low temperatures as values, sorted in 
            ascending order based on the average high temperatures.
    """
    return dict(sorted(city_temperatures.items(), key=lambda item: item[1][0]))