"""
QUESTION:
Design a function called `min_absolute_difference` that takes two lists of integers `list1` and `list2` as parameters and returns the minimum absolute difference between two elements of the two lists. The absolute difference between two integers a and b is given by |a - b|.
"""

def min_absolute_difference(list1, list2):
    min_diff = float('inf')
    for i in list1:
        for j in list2:
            diff = abs(i - j)
            if diff < min_diff:
                min_diff = diff
    return min_diff