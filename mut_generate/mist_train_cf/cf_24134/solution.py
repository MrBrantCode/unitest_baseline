"""
QUESTION:
Create a function `remove_duplicates` that takes a list of elements as input and returns a new list containing the same elements but with all duplicates removed. The order of the elements in the original list should be preserved. The function should not use any built-in functions that remove duplicates or convert the list to a set.
"""

def remove_duplicates(arr):
    res = []
    for x in arr: 
        if x not in res: 
            res.append(x)
    return res