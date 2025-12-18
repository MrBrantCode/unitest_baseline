"""
QUESTION:
Implement a function `unique_subsequence(arr: List[str])` that identifies the shortest unique subsequence in a list of input strings, considering case sensitivity and special characters. The function should handle identical strings in the list and return the shortest unique subsequence. The time complexity of the solution should not exceed O(n^2), where n is the length of each string in the list.
"""

from typing import List

def unique_subsequence(arr: List[str]) -> str:
    res = ""
    min_length = float('inf')
    for string in arr:
        for length in range(1, len(string) + 1):
            for i in range(len(string) - length + 1):
                subsequence = string[i:i + length]
                if sum(subsequence in s for s in arr) == 1 and len(subsequence) < min_length:
                    min_length = len(subsequence)
                    res = subsequence
    if min_length==float('inf'):
        res="No unique subsequence found"
    return res