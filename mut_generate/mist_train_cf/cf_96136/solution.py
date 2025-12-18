"""
QUESTION:
Create a function `remove_duplicates` that takes a list `arr` containing integers and/or strings as input and returns a list containing only the unique elements from `arr` in their original order. Do not include duplicate elements in the output list, even if they appear multiple times in the original list.
"""

def remove_duplicates(arr):
    seen = set()
    output = []
    
    for e in arr:
        if e not in seen:
            output.append(e)
            seen.add(e)
    
    return output