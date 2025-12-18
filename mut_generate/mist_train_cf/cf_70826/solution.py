"""
QUESTION:
Given a function `smallest_change` that takes an integer array `arr` and an integer `limit`, determine the least possible elements to adjust in order to render the array a palindrome. The function can alter one element to any other element in a single change and is restricted to a limited number of unique element changes.
"""

def smallest_change(arr, limit):
    left = 0
    right = len(arr) - 1
    mismatches = 0

    while left < right:
        if arr[left] != arr[right]:
            mismatches += 1
            if mismatches > limit:
                return mismatches

        left += 1
        right -= 1
    
    return mismatches