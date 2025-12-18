"""
QUESTION:
Write a function that applies a given mathematical formula to each element of a list of integers using the map() function. The function should take a list of integers as input, apply the formula x^2 + 2x + 1 to each element, and return a new list with the results.
"""

def entrance(nums):
    def complex_formula(num):
        return num ** 2 + 2 * num + 1
    return list(map(complex_formula, nums))