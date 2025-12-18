"""
QUESTION:
Create a function `solve` that takes a list of tuples as input. The function should return a nested dictionary where the keys are unique items from the first element of the tuple and their values are dictionaries. These inner dictionaries should have unique items from the second element of the tuple as keys and values will be their frequency count.
"""

from collections import defaultdict

def entrance(lst):
    result = defaultdict(lambda: defaultdict(int))
    for item, color in lst:
        result[item][color] += 1
        
    return dict(result)