"""
QUESTION:
Given a function `smallest_change(arr, limit)`, return the minimum number of unique element alterations required to convert the input array `arr` into a palindrome, where each unique element can be altered at most `limit` times. The function should return -1 if it is not possible to convert the array into a palindrome within the given limit.
"""

from collections import defaultdict

def smallest_change(arr, limit):
    left, right = 0, len(arr) - 1
    counts = defaultdict(int)
    unique_changes = 0
    total_changes = 0
    
    while left <= right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        elif arr[left] > arr[right]:
            if counts[arr[left]] < limit:
                total_changes += 1
                counts[arr[left]] += 1
                arr[right] = arr[left]
                left += 1
                right -= 1
            else:
                return -1
        else:
            if counts[arr[right]] < limit:
                total_changes += 1
                counts[arr[right]] += 1
                arr[left] = arr[right]
                left += 1
                right -= 1
            else:
                return -1
    return total_changes