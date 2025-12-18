"""
QUESTION:
Create a function named `modified_bubble_sort` that takes a list of integers as input and sorts only the elements at even indices in ascending order, leaving the elements at odd indices unchanged. The function should return the modified list. The input list may contain duplicate elements and may not be sorted initially.
"""

def modified_bubble_sort(lst):
    n = len(lst)
    
    for i in range(0, n, 2):
        for j in range(0, n-i-2, 2):
            if lst[j] > lst[j+2]:
                lst[j], lst[j+2] = lst[j+2], lst[j]
    
    return lst