"""
QUESTION:
Write a function `smallest_change(arr)` that takes a list of integers `arr` as input and returns the minimum number of modifications required to transform `arr` into a palindromic list, where a palindromic list is a list that reads the same backward as forward. Each modification involves changing a single element to any chosen value.
"""

def smallest_change(arr):
    n = len(arr)
    changes = 0

    # Use two pointers approach to compare elements from the start and end of the list
    i, j = 0, n - 1

    while i < j:
        # If the elements are not equal, we need to change one of them
        if arr[i] != arr[j]:
            changes += 1
        # Move the start pointer to the next element from the start
        i += 1
        # Move the end pointer to the next element from the end
        j -= 1
    return changes