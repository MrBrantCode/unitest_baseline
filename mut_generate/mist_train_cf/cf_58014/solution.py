"""
QUESTION:
Create a function `product_except_max` that calculates the product of all elements in a given list of integers except for the largest one. The function should handle lists with more than one element and return an error message if the list has only one element or is empty. If there are multiple maximum values, the function should exclude all of them. The input list will only contain integers.
"""

def product_except_max(lst):
    if len(lst) > 1:       # check if the list has more than one element
        max_val = max(lst) # find the max value
        while max_val in lst: # remove all occurrences of max value
            lst.remove(max_val)
        product = 1
        for i in lst: # for the remaining list, find the product
            product *= i
        return product
    else:
        return "List should have more than one integer"