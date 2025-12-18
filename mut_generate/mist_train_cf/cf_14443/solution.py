"""
QUESTION:
Write a function `remove_element(x, y)` that takes an element `x` and a list `y` as input, removes all occurrences of `x` from `y`, and returns the resulting list while maintaining the original order of the remaining elements. The function should have a time complexity of O(n), where n is the length of the list `y`.
"""

def remove_element(x, y):
    result = []
    for i in y:
        if i != x:
            result.append(i)
    return result