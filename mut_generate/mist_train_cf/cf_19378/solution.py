"""
QUESTION:
Implement a function `quick_sort(arr)` that takes a list of numbers as input and returns the sorted list in non-decreasing order. The function should have a time complexity of O(nlogn) and a space complexity of O(logn), where n is the size of the input list. The input list may contain duplicate numbers and negative numbers.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    smaller, equal, larger = [], [], []
    
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    
    return quick_sort(smaller) + equal + quick_sort(larger)