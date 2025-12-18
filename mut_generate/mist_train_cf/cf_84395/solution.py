"""
QUESTION:
Create a function called 'smallest_change' that takes two parameters: an integer array 'arr' and a limit representing the maximum number of changes allowed, which cannot exceed 50% of the array's length. This function should return the minimum number of elements that must be manipulated for the array to become palindromic, or -1 if it is impossible to do so within the given limit.
"""

def smallest_change(arr, limit):
    if limit > len(arr) // 2:
        limit = len(arr) // 2
    i, j = 0, len(arr)-1
    count = 0
    while i < j:
        if arr[i] != arr[j]:
            count += 1

            if count > limit:
                return -1

            arr[j] = arr[i]
        i += 1
        j -= 1
    return count