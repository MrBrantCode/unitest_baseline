"""
QUESTION:
Write a Python function called `count_elements` that takes a list as input, where the list can contain both integers and strings. The function should return a dictionary where the keys are the unique elements in the list and the values are the number of times each element appears in the list.
"""

def count_elements(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d