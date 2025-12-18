"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of integers as input, sorts the list in ascending order without using the built-in sort() method or any sorting algorithm library, and handles duplicate values efficiently. The function should return the sorted list.
"""

def bubble_sort(lst):
    n = len(lst)
    
    for i in range(n):
        for j in range(0, n - i - 1):
        
            if lst[j] > lst[j + 1] :
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  

    return lst