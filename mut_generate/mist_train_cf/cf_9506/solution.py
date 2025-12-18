"""
QUESTION:
Design a function called `quick_sort` that sorts an array of integers in ascending order using the Quick Sort algorithm. The function should take an array `arr` as input and return the sorted array. The Quick Sort algorithm should use the last element of the array as the pivot, and it should handle duplicate elements by keeping them in their original order.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) - 1]  
    smaller, equal, larger = [], [], []
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num > pivot:
            larger.append(num)
        else:
            equal.append(num)
    return quick_sort(smaller) + equal + quick_sort(larger)