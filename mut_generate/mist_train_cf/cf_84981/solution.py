"""
QUESTION:
Develop a function `quickSort(arr)` to implement the QuickSort algorithm, which sorts an array of elements in ascending order. The function should recursively divide the array into sub-arrays based on a chosen pivot element and return the sorted array. The pivot element is the middle element of the array. The function should be able to handle arrays of any size, including empty arrays. The input array can contain duplicate elements.
"""

def entance(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return entance(left) + middle + entance(right)