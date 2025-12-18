"""
QUESTION:
Implement a function `longest_sequence` that takes a sorted array of integers of length N (1 ≤ N ≤ 4) as input and returns the longest sequence of consecutive integers in the array. If no such sequence exists, the function should return an empty array.
"""

def longest_sequence(arr):
    if len(arr) < 2:
        return []
    longest = []
    current = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            current.append(arr[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [arr[i]]
    if len(current) > len(longest):
        longest = current
    return longest if len(longest) > 1 else []