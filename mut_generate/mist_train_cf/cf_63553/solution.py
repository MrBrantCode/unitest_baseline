"""
QUESTION:
Implement a function named `selection_sort` that sorts a list in non-decreasing order. The function should be able to handle potential duplicates in the list.
"""

def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst