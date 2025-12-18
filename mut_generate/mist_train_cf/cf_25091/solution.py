"""
QUESTION:
Create a function `get_even_elements` that takes a list of integers as input and returns a new list containing only the even elements from the input list.
"""

def get_even_elements(lst):
    return [i for i in lst if i % 2 == 0]