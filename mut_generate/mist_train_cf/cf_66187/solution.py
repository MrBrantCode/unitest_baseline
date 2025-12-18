"""
QUESTION:
Write a function `get_even_numbers` that takes a 2D list of integers as input and returns a new 2D list containing only the even numbers from the input list, preserving the original structure. The input list will contain at least one sub-list.
"""

def get_even_numbers(matrix):
    return [[num for num in row if num % 2 == 0] for row in matrix]