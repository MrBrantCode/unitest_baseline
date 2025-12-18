"""
QUESTION:
Write a function named `are_elements_unique` that takes a list as input and returns `True` if all elements in the list are unique and `False` otherwise, without using any additional data structures, with a time complexity of O(n^2) and a space complexity of O(1).
"""

def are_elements_unique(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True