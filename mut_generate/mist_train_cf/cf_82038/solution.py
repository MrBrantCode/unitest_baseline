"""
QUESTION:
Implement a function `remove_duplicates` that takes a sorted list of integers `numbers` and an integer `threshold` as input. The function should use binary search and recursion to remove elements from the list that appear more than `threshold` times, while preserving the original order of the remaining elements. The function should return the modified list.
"""

from typing import List

def remove_duplicates(numbers: List[int], threshold: int) -> List[int]: 
    """
    Reduce a sorted integer array by removing elements that exceed a set count, while preserving order.
    """
    def binary_search(low: int, high: int, x: int) -> int:
        """Find the rightmost occurrence of x in numbers."""
        if high >= low:
            mid = low + (high - low) // 2
            if (mid == len(numbers) - 1 or x < numbers[mid + 1]) and numbers[mid] == x:
                return mid
            elif x < numbers[mid]:
                return binary_search(low, mid - 1, x)
            else:
                return binary_search(mid + 1, high, x)
        return -1

    i = 0
    while i < len(numbers):
        first_occ = i
        last_occ = binary_search(i, len(numbers) - 1, numbers[i])
        if last_occ - first_occ + 1 > threshold:
            numbers = numbers[:first_occ] + numbers[last_occ + 1:]
            i = first_occ
        else:
            i = last_occ + 1
    return numbers