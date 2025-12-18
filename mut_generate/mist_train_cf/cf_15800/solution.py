"""
QUESTION:
Create a function called `shuffle_array` that takes an array of numbers as input. The function should return a new array where no two adjacent numbers are the same. The function must run in O(n log n) time complexity and use constant extra space. The input array can be modified.
"""

def shuffle_array(arr):
    arr.sort()
    result = []
    i, j = 0, 1
    
    while i < len(arr):
        result.append(arr[i])
        if j < len(arr):
            result.append(arr[j])
        i += 2
        j += 2

    return result