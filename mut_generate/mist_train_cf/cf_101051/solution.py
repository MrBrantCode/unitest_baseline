"""
QUESTION:
Create a function called `count_fuel_efficient_cars` that takes a list of tuples, where each tuple contains a car's name and its fuel efficiency in miles per gallon, and returns the number of cars with a fuel efficiency greater than 30 miles per gallon. The function should also print the names and fuel efficiencies of the cars that meet the criteria.
"""

def count_fuel_efficient_cars(cars):
    """
    This function takes a list of tuples containing car names and their fuel efficiencies.
    It returns the number of cars with a fuel efficiency greater than 30 miles per gallon and prints their names and fuel efficiencies.

    Args:
        cars (list): A list of tuples, where each tuple contains a car's name and its fuel efficiency in miles per gallon.

    Returns:
        int: The number of cars with a fuel efficiency greater than 30 miles per gallon.
    """

    count = 0

    for car, efficiency in cars:
        if efficiency > 30:
            count += 1
            print(f"{car}\t\t{efficiency}")

    return count