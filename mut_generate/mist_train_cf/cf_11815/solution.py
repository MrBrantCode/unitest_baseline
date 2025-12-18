"""
QUESTION:
Implement a function called bubble_sort that takes a list of integers as input and returns the sorted list in ascending order. The function should not use any built-in sorting functions or methods. The function should modify the original list by repeatedly swapping adjacent elements if they are in the wrong order.
"""

def bubble_sort(lst):
    n = len(lst)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst