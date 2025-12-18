"""
QUESTION:
Create a function called `sort_array` that takes an array of positive integers as input and returns the sorted array in descending order using a recursive approach with a time complexity of O(n) and constant space complexity, without using any additional arrays or data structures.
"""

def sort_array(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    return sort_array(greater) + [pivot] + sort_array(lesser)