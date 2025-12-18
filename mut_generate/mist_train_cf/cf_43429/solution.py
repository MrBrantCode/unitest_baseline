"""
QUESTION:
Implement a version of the QuickSort algorithm for a double-ended queue (deque) that can handle a mix of data types, such as integers and strings, without causing runtime errors. The function should take a deque as input and return the sorted deque. The sorting order should consider all strings as greater than any number. The implementation should be efficient in terms of time and space complexity.
"""

from collections import deque

def type_aware_compare(item1, item2):
    type1, type2 = type(item1), type(item2)
    
    if type1 == type2:
        return item1 < item2
    elif isinstance(item1, str): # strings are considered greater than integers
        return False
    else:
        return True      

def entrance(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        left = deque([x for x in data if type_aware_compare(x, pivot)])
        middle = deque([x for x in data if x == pivot])
        right = deque([x for x in data if type_aware_compare(pivot, x)])
        return entrance(left) + middle + entrance(right)