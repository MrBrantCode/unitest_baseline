"""
QUESTION:
Implement the `selection_sort` function to sort a list of integers in ascending order. The function should take one argument, a list of integers, and return the sorted list. The selection sort algorithm should repeatedly find the minimum element from the unsorted part of the list and swap it with the first element of the unsorted part.
"""

def selection_sort(lst):
    for i in range(len(lst)):
        minimum_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minimum_index]:
                minimum_index = j
        lst[i], lst[minimum_index] = lst[minimum_index], lst[i]
    return lst