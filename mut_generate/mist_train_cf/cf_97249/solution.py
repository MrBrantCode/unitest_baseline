"""
QUESTION:
Create a function `multiply_lists(list1, list2)` that takes two lists of the same length containing only positive integers and returns a new list where each element is the product of the corresponding elements in the input lists. The function should return an error message if the input lists are empty, have different lengths, or contain non-positive integers.
"""

def multiply_lists(list1, list2):
    if not list1 or not list2:
        return "Error: Input lists cannot be empty."

    if len(list1) != len(list2):
        return "Error: Input lists must have the same length."

    if any(num <= 0 for num in list1) or any(num <= 0 for num in list2):
        return "Error: Input lists should only contain positive integers."

    return [a * b for a, b in zip(list1, list2)]