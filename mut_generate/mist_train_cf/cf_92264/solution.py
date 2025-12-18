"""
QUESTION:
Create a function called `check_unique_ascending` that takes a list of elements as input. The function should return `True` if all elements in the list are unique and in ascending order, and `False` otherwise. The time complexity of the solution should be less than O(n^2).
"""

def check_unique_ascending(lst):
    if len(lst) != len(set(lst)):
        return False
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True