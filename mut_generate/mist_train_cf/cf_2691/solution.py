"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of integers as input and returns the list with duplicate integers removed. The function must not use any built-in functions or additional data structures, and must have a time complexity of O(n^2) and a space complexity of O(1). The list may contain negative numbers and is not sorted in ascending order.
"""

def remove_duplicates(lst):
    n = len(lst)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if lst[i] == lst[j]:
                # Remove duplicate element
                lst.pop(j)
                n -= 1
            else:
                j += 1
        i += 1
    return lst