"""
QUESTION:
Write a function that applies a complex mathematical formula to each element in a given list of integers using the map() function. The complex mathematical formula is f(x) = x^2 + 2x + 1. The function should return a new list containing the results of the formula applied to each element in the input list.
"""

def entrance(nums):
    def complex_formula(num):
        return num ** 2 + 2 * num + 1
    return list(map(complex_formula, nums))