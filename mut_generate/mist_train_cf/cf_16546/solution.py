"""
QUESTION:
Write a function named `square_even_numbers` that takes a list of integers as input and returns a new list containing the squares of the even numbers greater than 2 in the input list.
"""

def square_even_numbers(a):
    return [x**2 for x in a if x%2 == 0 and x > 2]