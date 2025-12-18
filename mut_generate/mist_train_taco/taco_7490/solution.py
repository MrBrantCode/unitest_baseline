"""
QUESTION:
Will you make it?

You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is ```50``` miles away! You know that on average, your car runs on about ```25``` miles per gallon. There are ```2``` gallons left. Considering these factors, write a function that tells you if it is possible to get to the pump or not. Function should return ``true`` (`1` in Prolog) if it is possible and ``false`` (`0` in Prolog) if not.
The input values are always positive.
"""

def can_reach_pump(distance_to_pump, mpg, fuel_left):
    """
    Determines if the car can reach the nearest fuel pump with the given fuel left.

    Parameters:
    - distance_to_pump (int/float): The distance to the nearest fuel pump in miles.
    - mpg (int/float): The average miles per gallon that the car can travel.
    - fuel_left (int/float): The amount of fuel left in gallons.

    Returns:
    - bool: True if the car can reach the pump, False otherwise.
    """
    return fuel_left >= distance_to_pump / mpg