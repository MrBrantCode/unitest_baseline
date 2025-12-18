"""
QUESTION:
Create a function called "removeDuplicates" that takes an array of integers as input. The function should return the modified array with duplicates removed. If the array contains any negative numbers, they should be sorted in descending order before removing duplicates. The function should return an empty array for input arrays that are empty or contain only duplicate values.
"""

def removeDuplicates(arr):
    if len(arr) == 0:
        return []
    
    if len(set(arr)) == 1:
        return []
    
    if any(x < 0 for x in arr):
        arr = sorted(arr, reverse=True)
        
    return sorted(list(set(arr)))