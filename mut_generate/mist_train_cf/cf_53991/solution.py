"""
QUESTION:
Create a function `calculate_sum(complex_list)` to calculate the sum of integers from a complex nested list using recursion and a for loop. The function should treat the complex list as if it was a simple list of integers. The complex list can contain other lists as elements, and these nested lists can also contain other lists as elements.
"""

def calculate_sum(complex_list):
    total = 0
    for element in complex_list:
        # if the element is list, calculate its sum recursively
        if isinstance(element, list):
            total += calculate_sum(element)
        else:
            total += element
    return total