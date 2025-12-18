"""
QUESTION:
Write a function `FunctionB` that takes a list of integers as input, returns a list of unique integers that are less than 50, and achieves a time complexity of O(n).
"""

def FunctionB(lst):
    result = set()    # using set instead of list to avoid duplicates
    for num in lst:
        if num < 50:
            result.add(num)    # using add method as we are now working with sets
    return list(result)    # converting back to list as return type