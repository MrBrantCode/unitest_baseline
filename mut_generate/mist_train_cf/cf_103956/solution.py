"""
QUESTION:
Implement a function called `descending_sort` that takes a list of integers as input and returns the list sorted in descending order. The function should have a time complexity of O(n^2), where n is the length of the input list.
"""

def descending_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(i+1, n):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst