"""
QUESTION:
Implement a recursive custom quicksort algorithm with the following characteristics:
- Choose the pivot element using the median-of-three method.
- Switch to insertion sort for small subarrays (less than or equal to 1 element).
Create a function `custom_quicksort(arr)` that takes an array as input and returns the sorted array.
"""

def custom_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = (arr[0] + arr[len(arr) // 2] + arr[-1]) // 3  # Median-of-three pivot selection
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return custom_quicksort(less) + equal + custom_quicksort(greater)