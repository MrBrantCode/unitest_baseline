"""
QUESTION:
Implement the function `quick_sort(arr)` that sorts a list of numbers in ascending order using the quick sort algorithm with a time complexity of O(nlogn) and a space complexity of O(logn). The function should handle lists with duplicate numbers and a large input size (n > 10^6).
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)