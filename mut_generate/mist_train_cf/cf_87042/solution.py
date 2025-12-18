"""
QUESTION:
Create a function `create_temperature_dict` that takes a dictionary of month names as keys and tuples of average high and low temperatures as values. The function should return a new dictionary sorted in ascending order based on the average high temperatures. The returned dictionary should maintain the month names as keys and tuples of average high and low temperatures as values.
"""

def create_temperature_dict(city_temperatures):
    return dict(sorted(city_temperatures.items(), key=lambda item: item[1][0]))