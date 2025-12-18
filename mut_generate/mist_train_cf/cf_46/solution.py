"""
QUESTION:
Implement a modified version of the quick-sort algorithm in Python that can handle duplicate elements, negative numbers, and sorts the array in descending order, while also keeping track of the number of comparisons made during the sorting process. 

The function should be named `quick_sort` and it should take an array `arr` as input, returning the sorted array and the number of comparisons made during the sorting process. The function should sort the array in descending order, with negative numbers appearing before positive numbers. 

However, there are two bugs in the implementation: one that causes incorrect sorting for arrays with an odd number of elements and another that causes incorrect sorting for arrays with duplicate elements.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        sorted_less, comparisons_less = quick_sort(less)
        sorted_greater, comparisons_greater = quick_sort(greater)
        comparisons = len(arr) - 1 + comparisons_less + comparisons_greater
        sorted_arr = sorted_greater + [pivot] + sorted_less
        return sorted_arr, comparisons