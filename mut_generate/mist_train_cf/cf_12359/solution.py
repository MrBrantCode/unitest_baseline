"""
QUESTION:
Create a function named `check_unique_ascending` that takes a list of elements as input. The function should return `True` if all elements in the list are unique and in ascending order, and `False` otherwise. The function should have a time complexity of less than O(n^2).
"""

def check_unique_ascending(lst):
    # Check for uniqueness using a set
    if len(lst) != len(set(lst)):
        return False
    
    # Check for ascending order using a for loop
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    
    return True