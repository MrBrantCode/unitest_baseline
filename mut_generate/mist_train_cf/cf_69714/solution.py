"""
QUESTION:
Write a function `smallest_change_in_subset(arr, limit, subset)` that takes an array of integers `arr`, an integer `limit`, and a list of integers `subset` as input. The function should return the minimum number of changes needed to make the array `arr` palindromic with no more than `limit` distinct element modifications, using only elements from the `subset`. A palindromic array reads the same in both directions, and you can change one array element to any other element from the `subset` per change. Assume that only those elements in `arr` are present in `subset` which are not part of a palindrome yet and need modification.
"""

from collections import Counter

def smallest_change_in_subset(arr, limit, subset):
    freq = Counter(arr)
    subs = set(subset)
    changes = 0
    l = 0
    r = len(arr) - 1
    while l <= r:
        while (l < len(arr) and arr[l] in subset):
            l += 1
        while (r > 0 and arr[r] in subset):
            r -= 1
        if (l <= r):
            changes += 1
            freq[arr[l]] -= 1
            freq[arr[r]] -= 1
            if freq[arr[l]] == 0:
                subs.remove(arr[l])
            if freq[arr[r]] == 0 and arr[r] in subs:
                subs.remove(arr[r])
            l += 1
            r -= 1
            if changes > limit:
                return min(changes, limit)
    return min(changes, limit)