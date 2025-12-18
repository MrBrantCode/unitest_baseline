"""
QUESTION:
Create a function `removeDuplicates(arr)` that takes an array of integers as input and returns a new array with all duplicates removed, preserving the original order of elements. The input array may be in any numerical order (ascending or descending) and may contain up to 10^6 elements with integer values ranging from -10^9 to 10^9. Do not use built-in functions for duplicate removal or sorting.
"""

def removeDuplicates(arr):
    dict_seen = {}
    out = []
    
    for num in arr:
        if num not in dict_seen:
            dict_seen[num] = True
            out.append(num)
            
    return out