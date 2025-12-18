"""
QUESTION:
Write a function called `does_it_fit` that takes two parameters: `a` (a tuple representing the dimensions of a car in the format (length, width)) and `b` (the total area of the parking lot). The function should return `True` if the car can fit in the parking lot and `False` otherwise. The car can fit if its dimensions are less than or equal to the dimensions of the parking lot (assuming the parking lot is a square) and the sum of its components (area) does not exceed the total area of the parking lot.
"""

def does_it_fit(a, b):
    if a[0]*a[1] <= b and a[0] <= b**0.5 and a[1] <= b**0.5:
        return True
    else:
        return False