"""
QUESTION:
Create a function called `sort_dictionary` that takes a dictionary with different types of keys and values as lists of numbers. The function should return a new dictionary with the same keys, but the values sorted in descending order.
"""

def sort_dictionary(dictionary):
    for key in dictionary:
        dictionary[key] = sorted(dictionary[key], reverse=True)
    return dictionary