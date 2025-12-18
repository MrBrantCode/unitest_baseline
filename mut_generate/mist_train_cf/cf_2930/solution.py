"""
QUESTION:
Write a function `join_dictionaries(d1, d2)` that takes two dictionaries `d1` and `d2` as input and returns a new dictionary where the keys are the intersection of the keys from `d1` and `d2`, and the values are the product of the corresponding values from `d1` and `d2`. The function should have a time complexity of O(n), where n is the number of keys in `d1`.
"""

def join_dictionaries(d1, d2):
    d3 = {}
    
    for key in d1:
        if key in d2:
            d3[key] = d1[key] * d2[key]
    
    return d3