"""
QUESTION:
Implement a recursive function `find_all_electric_cars` that takes a list of car models and returns a list of names of all-electric vehicles with a range of at least 200 miles per charge. The returned list should be sorted in alphabetical order. The function should not print the names directly, but instead return the sorted list of names. Assume the list of car models is in the format `[{'name': str, 'type': str, 'range': int}, ...]`.
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