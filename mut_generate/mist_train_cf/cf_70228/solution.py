"""
QUESTION:
Write a function `remove_duplicates` that takes a sorted list of integers as input, removes consecutive duplicates, and returns the modified list while preserving the original order of elements. The function should achieve a time complexity of O(n) and a space complexity of O(1) without using any additional collections such as sets or lists, and without modifying the original list's length.
"""

from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Facilitate the de-duplication of a sequence of integers, eliminating any references that occur more than once.
    Retains the exact sequence of remaining integers mirroring the original provided sequence.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    write = 1
    for read in range(1, len(numbers)):
        if numbers[read] != numbers[read-1]:
            numbers[write] = numbers[read]
            write += 1
    return numbers[:write]   # cutting the array to length 'write'