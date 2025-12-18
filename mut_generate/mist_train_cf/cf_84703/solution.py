"""
QUESTION:
Implement a function named `find_constrictive` that takes a list of integers as input and returns the indices of all "constrictive" elements. A "constrictive" element is defined as an element for which the sum of all previous elements is equal to the product of all subsequent elements. 

The function should handle edge cases, including an empty list and a single-element list, by returning error messages. If no "constrictive" element is found, the function should return a corresponding message. If multiple "constrictive" elements are found, the function should return all their indices.
"""

from functools import reduce
from operator import mul

def find_constrictive(lst):
    if len(lst)==0:
        return 'Error: List is empty!'
    if len(lst)==1:
        return 'Error: List contains only one element!'
    
    constrictive_indices=[]
    
    for i in range(len(lst)):
        left_sum = sum(lst[:i]) if i > 0 else 0
        right_product = reduce(mul, lst[i+1:], 1)
        
        if left_sum == right_product:   
            constrictive_indices.append(i)
    
    if len(constrictive_indices)==0:
       return 'No constrictive element found'
    else:
       return constrictive_indices