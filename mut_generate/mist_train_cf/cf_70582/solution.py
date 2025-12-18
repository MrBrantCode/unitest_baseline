"""
QUESTION:
Implement a function `bubble_sort` that takes a list of integers as input and returns the list sorted in ascending order, allowing for duplicate values. The function should use the Bubble Sort algorithm, which repeatedly swaps adjacent elements if they are in the wrong order, until no more swaps are needed.
"""

def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j+1] :
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list