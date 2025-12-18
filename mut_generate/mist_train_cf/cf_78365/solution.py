"""
QUESTION:
Implement the `next_smallest` function, which takes a list of integers as input and returns the second smallest element in the list. If the list has less than two unique elements, return `None`. The function should be efficient and work for lists of any size.
"""

def next_smallest(lst):
    
    if len(lst) < 2:
        return None
    
    lst.sort()
    
    smallest = lst[0]
    
    for el in lst:
        if el > smallest:
            return el
    
    return None