"""
QUESTION:
Write a function called `remove_duplicates` that takes a list containing integers and strings as input, removes duplicates while maintaining the original order of the first appearance of each element, and returns the resulting list. The function should not use any built-in functions like `set` or `dict` that automatically remove duplicates, but instead use list comprehension.
"""

def remove_duplicates(lst):
    res = []
    [res.append(i) for i in lst if i not in res]
    return res