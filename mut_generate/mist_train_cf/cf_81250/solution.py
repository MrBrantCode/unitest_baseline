"""
QUESTION:
Write a function `empty_seats` that takes three parameters: the total number of bus seats, and two float values representing the percentage of occupied and reserved seats. Calculate the number of empty seats based on these percentages, considering cases where the total percentage of occupied and reserved seats exceeds 100%. If the total percentage exceeds 100%, return an error message. The function should also handle edge cases where the percentages are 0 or 1, or where they add up to exceed 1. Assume that the input values for the number of seats and the rates are valid non-negative numbers.
"""

def empty_seats(bus_seats, occupied_rate, reserved_rate):
    occupied_seats = bus_seats * occupied_rate
    reserved_seats = bus_seats * reserved_rate
    if occupied_seats + reserved_seats > bus_seats:
        return 'Error: The number of occupied and reserved seats cannot exceed the total number of seats.'
    empty_seats = bus_seats - occupied_seats - reserved_seats
    return round(empty_seats)