"""
QUESTION:
Write a function named `count_items` that takes a dictionary as input and returns the total number of items in the dictionary, including items in any nested dictionaries. The function should recursively count the items at all levels of nesting.
"""

def count_items(dictionary):
    count = len(dictionary)  

    for value in dictionary.values():
        if isinstance(value, dict):  
            count += count_items(value)  

    return count