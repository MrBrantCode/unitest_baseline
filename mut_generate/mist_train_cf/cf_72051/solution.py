"""
QUESTION:
Given an integer array `arr` and a limit on the number of unique changes `limit`, find the minimum number of elements to alter to make the array into a palindrome, with the constraint that one element can be changed to any other element in a single move. The function should be named `minimum_changes` and take two parameters: `arr` and `limit`.
"""

from collections import Counter

def minimum_changes(arr, limit):
    counter = Counter(arr)
    counts = sorted(list(counter.values()), reverse=True)
    
    res = 0
    while len(counts) > limit:
        res += counts.pop()
        
    return res