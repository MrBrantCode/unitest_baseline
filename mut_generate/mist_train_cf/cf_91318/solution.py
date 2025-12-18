"""
QUESTION:
Write a function `sum_of_squares_of_even_numbers` that takes a list of integers as an argument and returns the sum of the squares of even numbers in the list. The function should only use a single loop to iterate through the list, and it cannot use any built-in Python functions or methods for finding even numbers or calculating squares.
"""

def sum_of_squares_of_even_numbers(lst):
    sum_of_squares = 0
    for num in lst:
        if num % 2 == 0:
            square = num * num
            sum_of_squares += square
    return sum_of_squares