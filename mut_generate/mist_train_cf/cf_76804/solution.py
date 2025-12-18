"""
QUESTION:
Given an array of integers `arr` and an integer `limit`, write a function `minimum_change_to_palindrome` to find the minimum number of elements required to change to form a palindrome, with the restriction that a single change can transform one element into any other element and the total number of changes for each distinct element cannot exceed `limit`.
"""

from collections import Counter

def minimum_change_to_palindrome(arr, limit):
    n = len(arr)
    ans = 0
    counter = Counter(arr)
    changes = {x: 0 for x in arr}
    for i in range(n//2):
        if arr[i] != arr[n-i-1]:
            changes[arr[i]] += 1
            changes[arr[n-i-1]] += 1
    for change in changes.values():
        if change < limit:
            ans += change // 2
    return ans