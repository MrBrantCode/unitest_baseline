"""
QUESTION:
Implement a function `mergeSort(arr)` that sorts an array of strings by their length in descending order. If two strings have the same length, they should be sorted lexicographically in descending order. The function should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def compareStrings(s1, s2):
    if len(s1) == len(s2):
        return -1 if s1 > s2 else 1
    return len(s2) - len(s1)

def merge(arr1, arr2):
    merged = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if compareStrings(arr1[i], arr2[j]) < 0:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge(left, right)