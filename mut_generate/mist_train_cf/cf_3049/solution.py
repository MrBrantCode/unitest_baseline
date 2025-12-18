"""
QUESTION:
Write a function `are_elements_unique` that determines if all elements in a list are unique without using any additional data structures other than the input list. The function should have a time complexity of O(n^2) and a space complexity of O(1). The input is a list of integers, and the output is a boolean value indicating whether all elements in the list are unique or not.
"""

def are_elements_unique(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] == lst[j]:
                return False
    return True