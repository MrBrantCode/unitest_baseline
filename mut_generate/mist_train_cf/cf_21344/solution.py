"""
QUESTION:
Create a function `generate_dictionary(list_a, list_b)` that takes two lists, list_a and list_b, as input where list_a contains unique elements and list_b contains strings, and the length of list_a is equal to the length of list_b. The function should return a dictionary with keys from list_a in ascending order and corresponding values from list_b in descending order.
"""

def generate_dictionary(list_a, list_b):
    return dict(sorted(zip(sorted(list_a), sorted(list_b, reverse=True))))