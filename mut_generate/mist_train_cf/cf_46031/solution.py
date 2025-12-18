"""
QUESTION:
Implement a function named `product_array` that takes one argument `lst` which is a list of numbers. The function should return the product of all the numbers in the list. However, if the list is empty, the function should return "Error: List is empty." If the list contains non-numeric values, the function should return "Error: List contains non-numeric values."
"""

def product_array(lst):
    if not lst:
        return "Error: List is empty."
        
    total = 1
    for i in lst:
        if not isinstance(i, (int, float)):
            return "Error: List contains non-numeric values."
        total *= i
    return total