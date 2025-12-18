"""
QUESTION:
Implement a function named `union` that takes two lists (`set1` and `set2`) as input and returns a new list containing their union. The resulting list should contain all unique elements from both input lists, maintaining their original order, and without using any built-in set functions or libraries.
"""

def union(set1, set2):
    result = list(set1)
    
    for element in set2:
        if element not in result:
            result.append(element)
            
    return result