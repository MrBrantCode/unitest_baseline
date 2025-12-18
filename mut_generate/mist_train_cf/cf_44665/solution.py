"""
QUESTION:
Implement a function `product_of_elements(arr)` that calculates the product of all elements in a given array. The function should handle the following edge cases: 
- an empty array
- non-integer values in the array
- integer overflow (the product exceeds the maximum limit of a 64-bit integer).
"""

def product_of_elements(arr):
    if not arr:  
        return None
    product = 1
    for elem in arr:
        try:
            elem = int(elem)   
            product *= elem
        except ValueError:
            return "All elements in the array should be integers"
        if product >= 2**63 - 1 or product <= -(2**63):    
            return "Int Overflow Error: The product of elements is out of range for int64."
    return product