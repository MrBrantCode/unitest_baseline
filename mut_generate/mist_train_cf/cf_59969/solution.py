"""
QUESTION:
Write a function `common_elements(l1, l2, l3)` that takes three lists as input and returns a list of elements that are common to all three lists under the same index. The function should handle lists of different lengths and return common elements up to the length of the shortest list. The function should also be able to handle lists containing different data types such as integers, strings, and floating point numbers.
"""

def common_elements(l1, l2, l3):
    common = []
    for a, b, c in zip(l1, l2, l3):   
        if a == b == c:                
            common.append(a)           
    return common