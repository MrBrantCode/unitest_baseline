"""
QUESTION:
Implement a function named `adaptive_quicksort(arr)` that takes a list of integers as input. The function should sort the list in ascending order using the quicksort algorithm, select the pivot based on the input data for optimal performance, and exclude any duplicate values from the list. The function should return the sorted list of unique integers. The input list can contain duplicate values and may be in any order.
"""

def adaptive_quicksort(arr):
    def Quicksort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr)//2]
            less = [x for x in arr if x < pivot]
            equal = [x for x in arr if x == pivot]
            greater = [x for x in arr if x > pivot]
            return Quicksort(less) + equal + Quicksort(greater)

    arr = list(set(arr))
    return Quicksort(arr)