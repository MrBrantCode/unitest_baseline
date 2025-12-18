"""
QUESTION:
Create a function `remove_duplicates` that takes a list of integers as input, raises each integer to the power of 3, removes duplicates, and returns the resulting list sorted in descending order based on the sum of the digits of the integers. If two integers have the same sum of digits, the negative integer should come before the positive integer.
"""

def remove_duplicates(lst):
    lst = list(set(map(lambda x: x ** 3, lst)))  # Remove duplicates and raise to power of 3
    lst.sort(key=lambda x: (-sum(int(digit) for digit in str(abs(x))), x < 0))  # Sort by sum of digits and negative/positive
    return lst