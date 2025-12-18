"""
QUESTION:
Write a function called `custom_sort` that takes a list of integers as input and returns the list sorted in descending order. The function should not use any built-in sorting functions or methods and should have a time complexity of O(n^2). The function should be able to handle lists containing negative integers, floating-point numbers, lists with duplicate integers, and lists of any length.
"""

def custom_sort(lst):
    length = len(lst)
    
    if length <= 1:
        return lst
    
    # Sort in ascending order
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    # Sort in descending order
    lst.reverse()
    
    return lst