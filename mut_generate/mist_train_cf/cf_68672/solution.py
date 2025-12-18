"""
QUESTION:
Create a function named `amplify_elements(array)` that takes a list of integers as input, removes duplicates by considering only distinctive elements, and returns a new list containing these elements multiplied by two.
"""

def amplify_elements(array):
    # amplifying each distinctive element by a multiplication factor of two
    # and storing it in a new list using list comprehension
    return [element*2 for element in set(array)]