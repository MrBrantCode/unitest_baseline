"""
QUESTION:
Create a function called `flat_list` that decompresses a deeply nested list into a single-level sequence. The function should be able to handle lists that are nested arbitrarily deep. The function should take one argument, `nested_list`, and return a one-dimensional list containing all elements from the original list.
"""

def flat_list(nested_list):
    result = []
    for i in nested_list:
        if isinstance(i, list):
            result += flat_list(i) 
        else:
            result.append(i)
    return result