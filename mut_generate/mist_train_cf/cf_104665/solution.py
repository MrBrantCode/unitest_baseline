"""
QUESTION:
Create a function called `remove_duplicates` that takes an array of integers and/or strings as input and returns a new array containing only the unique elements from the original array, in the original order. The function should not modify the original array.
"""

def remove_duplicates(arr):
    """Returns a new array containing only the unique elements from the original array, in the original order."""
    element_counts = {}
    output = []
    
    for e in arr:
        if e not in element_counts:
            element_counts[e] = 1
        else:
            element_counts[e] += 1
    
    for e in arr:
        if e in element_counts and element_counts[e] == 1:
            output.append(e)
            del element_counts[e]
    
    return output