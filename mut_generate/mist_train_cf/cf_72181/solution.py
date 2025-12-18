"""
QUESTION:
Write a function named `solve` that takes a 2D array `arr` as input and returns the total number of non-repeating elements in the array. The function should not count repeating elements across all sublists.
"""

def solve(arr):
    s = set()
    for sublist in arr:
        for i in sublist:
            if i not in s:
                s.add(i)
    return len(s)