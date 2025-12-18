"""
QUESTION:
Write a function `flatten_and_join` that takes a 2D list of integers as input and returns a string of comma-separated values. The input list is a list of lists, where each sublist contains integers. The function should flatten the input list into a single list and then convert it into a string of comma-separated values.
"""

def flatten_and_join(array):
    return ','.join([str(item) for sublist in array for item in sublist])