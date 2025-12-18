"""
QUESTION:
Write a function named `search_python` that takes a nested list and a target string 'python' as input, and returns the count of the number of occurrences of 'python' within the list. The function should be case-sensitive and able to handle lists nested to any depth.
"""

def search_python(nested_list, target ='python'):
    count = 0
    for i in nested_list:
        if isinstance(i, list):
            count += search_python(i, target)
        elif i == target:
            count += 1
    return count