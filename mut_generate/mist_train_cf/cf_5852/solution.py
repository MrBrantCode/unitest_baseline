"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of elements (integers and/or strings) as input and returns a list containing only the unique elements in the original order. The function should also sort the unique elements based on their types, with integers before strings.
"""

def remove_duplicates(arr):
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
            
    output.sort(key=lambda x: (isinstance(x, int), x))
    
    return output