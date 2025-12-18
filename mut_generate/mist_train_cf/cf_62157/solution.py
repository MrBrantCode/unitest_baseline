"""
QUESTION:
Create a function `can_it_float(x, y)` that takes an array `x` and a volume limit `y` as input. The function should return `True` if the array elements are all identical and the sum of the array elements does not exceed the volume limit `y`, and `False` otherwise.
"""

def can_it_float(x, y):
    # check if all elements in the array are the same
    uniformity = all(el == x[0] for el in x)
    # check if sum of all elements is less or equal to the acceptable volume
    volume = sum(x) <= y
    # return True if both conditions are met, else return False
    return uniformity and volume