"""
QUESTION:
Implement a parallel quicksort function `parallel_quick_sort` that takes a list of integers as input and returns the sorted list, utilizing multiple CPU cores to speed up the sorting process. The function should minimize unnecessary computations and handle large lists efficiently.
"""

def parallel_quick_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        pivot = unsorted_list[0]
        less_elements = [element for element in unsorted_list[1:] if element <= pivot]
        more_elements = [element for element in unsorted_list[1:] if element > pivot]
        return parallel_quick_sort(less_elements) + [pivot] + parallel_quick_sort(more_elements)