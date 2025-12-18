"""
QUESTION:
Implement the `quick_sort(arr)` function to sort a list of numbers in ascending order with a time complexity of O(nlogn) and space complexity of O(logn), handling large input sizes (n > 10^6) and duplicate numbers.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)