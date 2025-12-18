"""
QUESTION:
Develop a function `product_of_values(data)` that calculates the product of all numeric values in a given list `data` of mixed data types, including nested lists and dictionaries. The function should ignore non-numeric values and handle complex numbers, returning the product in the form of a complex number if any of the values in the list are complex.
"""

def product_of_values(data):
    product = 1
    if isinstance(data, (list, tuple)):  
        for item in data:
            product *= product_of_values(item)
    elif isinstance(data, dict):  
        for item in data.values():
            product *= product_of_values(item)
    elif isinstance(data, (int, float, complex)):  
        product *= data
    return product