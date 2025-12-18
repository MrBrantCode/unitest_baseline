"""
QUESTION:
Create a function named `filter_red_toyotas` that takes a list of dictionaries representing cars, each with keys 'brand', 'year', and 'color', and returns a list of cars that are of the brand 'Toyota', with a year greater than 2010, and a color of 'red'. The function must iterate through the list only once.
"""

def filter_red_toyotas(cars):
    return [car for car in cars if car['brand'] == 'Toyota' and car['year'] > 2010 and car['color'] == 'red']