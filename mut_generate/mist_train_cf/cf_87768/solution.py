"""
QUESTION:
Create a function named `are_elements_unique` that takes a list of integers as input and returns a boolean value indicating whether all elements in the list are unique or not. The function should have a time complexity of O(n^2) and a space complexity of O(1). Note that no additional data structures other than a constant amount of space are allowed.
"""

def are_elements_unique(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True