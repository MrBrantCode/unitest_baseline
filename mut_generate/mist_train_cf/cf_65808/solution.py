"""
QUESTION:
Write a function `MinimumChangesToPalindrome` that takes a slice of integers `arr` and an integer `limit` as input. The function should return the minimum number of changes required to make the slice a palindrome, with a constraint that at most `limit` unique elements can be modified. The function should modify the larger element at the ends of the slice to the smaller one. If the number of unique modifications exceeds the limit, the function should return the current number of changes.
"""

def MinimumChangesToPalindrome(arr, limit):
    i, j = 0, len(arr) - 1
    changes = 0
    unique_elements = set()

    while i < j:
        if arr[i] != arr[j]:
            changes += 1
            if arr[i] not in unique_elements:
                limit -= 1
                if limit < 0:
                    return changes
                unique_elements.add(arr[i])
            arr[j] = arr[i]
        i += 1
        j -= 1
    return changes