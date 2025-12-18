"""
QUESTION:
Create a function named `standard_deviation` that takes a list of integers as input and calculates the standard deviation without using any built-in functions or libraries. The list contains n integers ranging from 1 to 10^3. The calculated standard deviation should be rounded to 2 decimal places.
"""

def standard_deviation(lst):
    n = len(lst)
    mean = sum(lst) / n
    variance = sum((x - mean) ** 2 for x in lst) / n
    res = variance ** 0.5
    return round(res, 2)