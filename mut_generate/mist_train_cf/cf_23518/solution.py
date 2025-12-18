"""
QUESTION:
Write a function called `quick_sort` that sorts a given array of elements in ascending order. The array can contain any number of elements, but all elements must be comparable. The function should return a new sorted array without modifying the original array.
"""

def quick_sort(arr): 
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)