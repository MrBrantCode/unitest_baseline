"""
QUESTION:
Create a function `remove_duplicates(arr: List[int]) -> List[int]` that removes duplicates from the input array and returns a new array with the remaining elements sorted in ascending order. The input array will not contain any negative numbers and will have a length of at most 100. The function should have a time complexity of O(n) and should not use any additional data structures or libraries beyond basic data structures and algorithms. The original array should remain unchanged.
"""

from typing import List

def remove_duplicates(arr: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    result.sort()
    return result