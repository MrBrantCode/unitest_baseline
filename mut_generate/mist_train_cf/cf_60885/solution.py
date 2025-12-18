"""
QUESTION:
Create a function named "bubble_sort" that takes two lists of equal length as input, sorts the first list in ascending order using the Bubble Sort technique without using any built-in "sort" function in Python, and simultaneously sorts the second list in the same way by swapping corresponding elements. The function should return the two sorted lists.

The input lists are not empty and contain elements that can be compared (e.g., integers). The function should not use any additional data structures that scale with input size. The function should run in a reasonable amount of time and use a reasonable amount of memory.
"""

def bubble_sort(lst1, lst2):
    n = len(lst1)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst1[j] > lst1[j+1] :
                lst1[j], lst1[j+1] = lst1[j+1], lst1[j]
                lst2[j], lst2[j+1] = lst2[j+1], lst2[j]  # Swapping elements in lst2 the same way as lst1
    
    return lst1, lst2