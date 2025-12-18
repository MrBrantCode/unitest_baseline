"""
QUESTION:
Construct a function named `generate_list` that takes in two lists, `list_one` and `list_two`. The function should generate a new list containing the product of elements from the two lists when the element from `list_one` is odd, and the element from `list_two` multiplied by 2 when the element from `list_one` is not odd. The function should use list comprehension to create the new list.
"""

def generate_list(list_one, list_two):
    return [a*b if a%2 != 0 else b*2 for a, b in zip(list_one, list_two)]