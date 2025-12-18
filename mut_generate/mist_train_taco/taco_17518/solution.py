"""
QUESTION:
After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).
"""

def calculate_rental_car_cost(days: int) -> int:
    """
    Calculate the total cost of renting a car for a given number of days.

    The base cost per day is $40. If the car is rented for 7 or more days, a $50 discount is applied.
    If the car is rented for 3 or more days but less than 7 days, a $20 discount is applied.

    :param days: The number of days the car is rented.
    :return: The total cost of renting the car.
    """
    total_cost = days * 40
    if days >= 7:
        total_cost -= 50
    elif days >= 3:
        total_cost -= 20
    return total_cost