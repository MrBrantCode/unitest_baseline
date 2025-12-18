"""
QUESTION:
Write a function called `even_numbers_with_index` that generates a list of tuples, where each tuple contains an even number and its index, from a given range of numbers. The function should take one argument, the end of the range (inclusive), and return the list of tuples.
"""

def even_numbers_with_index(end):
    return [(i, index) for index, i in enumerate(range(end + 1)) if i % 2 == 0]