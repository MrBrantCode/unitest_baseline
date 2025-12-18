"""
QUESTION:
Write a function called `calculate_sum` that takes a potentially nested list of elements as input. Calculate the sum of all numeric elements (integers and floats) in the list, ignoring non-numeric elements. Implement the sum calculation logic manually without using built-in functions like `sum()`. If the input list is nested, the function should recursively flatten the list and consider all elements for calculation.
"""

def calculate_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, (int, float)):
            total += element
        elif isinstance(element, list):
            total += calculate_sum(element)
    return total