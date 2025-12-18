"""
QUESTION:
Implement a function `bubble_sort(lst)` that sorts a list of integers into ascending order without using built-in sorting functions or libraries, with a time complexity of O(n^2). The function should handle duplicate values and negative numbers.
"""

def entrance(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst