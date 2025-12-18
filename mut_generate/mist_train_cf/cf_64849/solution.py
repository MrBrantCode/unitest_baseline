"""
QUESTION:
Given a list of integers `arr`, write a function `checkIfExist` that checks if there exist two integers `N` and `M` in `arr` such that `N` is the triple of `M` (i.e., `N = 3 * M`). The function should return `True` if such integers exist and `False` otherwise. The list `arr` will have a length between 2 and 500, inclusive, and will contain integers between -10^3 and 10^3, inclusive.
"""

def checkIfExist(arr):
    elements = set()
    for num in arr:
        if num * 3 in elements or (num % 3 == 0 and num // 3 in elements):
            return True
        elements.add(num)
    return False