"""
QUESTION:
Implement the function `quick_sort(arr)` that sorts a list of integers in ascending order. The list can contain negative numbers and duplicates, with values ranging from -1000 to 1000. The function should be able to efficiently handle lists with up to 1 million elements.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)