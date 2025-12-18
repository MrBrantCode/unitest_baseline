"""
QUESTION:
Create a recursive function `find_all_electric_cars` that takes a list of car models as input, where each car model is a dictionary containing 'name', 'type', and 'range' information. The function should return a list of names of all-electric vehicles with a range of 200 miles or more per charge, sorted in alphabetical order.
"""

def find_all_electric_cars(cars, index=0, electric_cars=None):
    if electric_cars is None:
        electric_cars = []

    if index >= len(cars):
        electric_cars.sort()
        return electric_cars

    car = cars[index]
    if car['type'] == 'electric' and car['range'] >= 200:
        electric_cars.append(car['name'])

    return find_all_electric_cars(cars, index + 1, electric_cars)