"""
QUESTION:
Write a function called `smallest_change_in_subset` that takes in three parameters: an array of integers `arr`, an integer `limit` representing the maximum number of unique element modifications allowed, and a subset of integers from `arr`. The function should return the minimum number of elements that need to be changed in `arr` to make it a palindrome, with the restriction that only elements from the given subset can be used for modification.
"""

def smallest_change_in_subset(arr, limit, subset):
    """
    Given an array 'arr', a set of integers, and a certain subset filled with these integers, determine the least
    number of elements that have to be altered within the limit of unique element modifications to 
    turn the 'arr' into a palindromic array, on the condition that only elements from the given subset can be used.
    A palindromic array is an array structure that remains the same when read in reverse order.
    A single change allows you to modify one element to any other unique element contained within the subset.
    """
    left, right = 0, len(arr) - 1
    count = 0
    while left < right:
        if arr[left] != arr[right]:
            if arr[left] not in subset or arr[right] not in subset:
                return -1  # or handle the case when the elements cannot be changed
            count += 1
        left += 1
        right -= 1
    return min(count, limit) if count <= limit * 2 else -1