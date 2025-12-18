"""
QUESTION:
Create a function called `count_key_value_pairs` that takes one parameter, a dictionary. The function must return the number of key-value pairs in the dictionary without using the built-in `len()` function.
"""

def count_key_value_pairs(dictionary):
    count = 0
    for key, value in dictionary.items():
        count += 1
    return count