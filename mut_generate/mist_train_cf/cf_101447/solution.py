"""
QUESTION:
Create a function named `filter_red_toyotas` that takes a list of dictionaries representing cars, where each dictionary contains 'brand', 'year', and 'color' keys. Return a new list containing only the cars that are of the brand 'Toyota', with a year greater than 2010, and a color of 'red'. The function should only iterate through the input list once.
"""

def filter_red_toyotas(cars):
    return [car for car in cars if car['brand'] == 'Toyota' and car['year'] > 2010 and car['color'] == 'red']