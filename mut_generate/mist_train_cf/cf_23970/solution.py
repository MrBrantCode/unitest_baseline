"""
QUESTION:
Implement a function named `quick_sort` that sorts an input array in descending order. The function should take an array of integers as input and return the sorted array. Note that the function should use the quicksort algorithm.
"""

def quick_sort(arr): 
    if len(arr) <= 1:
        return arr
  
    pivot = arr[-1]
    lesser_elements = [i for i in arr[:-1] if i <= pivot]
    greater_elements = [i for i in arr[:-1] if i > pivot]
    return quick_sort(greater_elements) + [pivot] + quick_sort(lesser_elements)