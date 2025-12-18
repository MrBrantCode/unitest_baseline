"""
QUESTION:
Create a function `distinct_elements_pairs` that takes a list of integers as input and returns a tuple of four values: the total number of distinct even integers, the total number of distinct odd integers, the sum of even integers squared, and the sum of odd integers squared. If there are no integers for a given condition, return it as zero.
"""

def distinct_elements_pairs(lst):
    even_count = len([i for i in set(lst) if i % 2 == 0])
    odd_count = len([i for i in set(lst) if i % 2 != 0])
    even_squared_sum = sum([i**2 for i in set(lst) if i % 2 == 0])
    odd_squared_sum = sum([i**2 for i in set(lst) if i % 2 != 0])
    return (even_count, odd_count, even_squared_sum, odd_squared_sum)