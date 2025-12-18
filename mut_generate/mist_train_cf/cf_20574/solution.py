"""
QUESTION:
Design a function named `remove_duplicates` that takes a list as input and returns a new list with all duplicate elements removed. The function should preserve the original order of elements and remove any elements that appear more than once in the input list, regardless of whether the duplicates are consecutive or not.
"""

def remove_duplicates(lst):
    unique = []
    counts = {}
    
    for item in lst:
        if item not in unique:
            unique.append(item)
        
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
            
    return [item for item in unique if counts[item] == 1]