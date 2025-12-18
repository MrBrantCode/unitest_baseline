"""
QUESTION:
Create a function `findSmallestMissing` that takes an array of integers as input, and returns the smallest positive integer not present in the array. The function should have a time complexity of O(n log n) and a space complexity of O(log n). The array can contain both positive and negative numbers. If no positive integer is missing, the function should return the smallest positive integer greater than the maximum element in the array.
"""

def findSmallestMissing(arr):
    arr.sort()
    
    smallest_missing = 1
    
    for num in arr:
        if num <= 0:
            continue
        
        if num == smallest_missing:
            smallest_missing += 1
        elif num > smallest_missing:
            return smallest_missing
    
    return smallest_missing