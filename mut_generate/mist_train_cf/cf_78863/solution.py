"""
QUESTION:
Create a function `negative_even_squares_sum(lst)` that takes a list of numbers as input and returns the sum of the squares of the numbers that are both negative and even. If the input list is empty or does not contain any negative even numbers, the function should return 0.
"""

def negative_even_squares_sum(lst):
    return sum(i*i for i in lst if i < 0 and i % 2 == 0)