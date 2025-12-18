"""
QUESTION:
Create a function `recursive_sum` that calculates the sum of all integers in a given list, including those in nested lists. The function should use recursion and have a time complexity of O(n), where n is the total number of elements in the list. If a nested list contains non-integer elements, they should be ignored in the sum calculation. The function should return the total sum of integers in the list.
"""

def recursive_sum(lst):
    if isinstance(lst, int):
        return lst
    elif isinstance(lst, list):
        return sum(recursive_sum(x) for x in lst if isinstance(x, (int, list)))
    else:
        return 0