"""
QUESTION:
Implement a function `minimum_changes(arr, limit)` that takes an array of integers and an integer `limit` as input, and returns the minimum number of elements that need to be altered to make the array a palindrome, with a constraint that the number of unique alterations (i.e., the number of distinct pairs of elements that are changed) is at most `limit`. If it's impossible to make the array a palindrome within the given limit, return -1.
"""

def min_changes(arr, limit):
    if arr == arr[::-1]:    # If array is already palindrome
        return 0

    n = len(arr)
    l = 0    # Define the left pointer
    r = n-1    # Define the right pointer
    counter = 0    # Count of changes made
    changes = set()    # Unique changes made

    while l <= r:
        # If elements are equal, move both pointers
        if arr[l] == arr[r]:
            l += 1
            r -= 1
        else:
            # If elements are not equal, increment counter, make them equal and check limit
            counter += 1
            changes.add((min(arr[l], arr[r]), max(arr[l], arr[r])))
            if len(changes) > limit:
                return -1
            arr[l] = arr[r] = min(arr[l], arr[r])
            l += 1
            r -= 1
    return counter