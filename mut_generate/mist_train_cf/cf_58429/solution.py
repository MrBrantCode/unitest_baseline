"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers and an integer threshold as input, and returns a new list with all elements that appear more than the given threshold removed, while maintaining the original order of elements. The function must have a time complexity of O(n).
"""

from typing import List
from collections import defaultdict

def remove_duplicates(numbers: List[int], threshold: int) -> List[int]:
    count = defaultdict(int)
    result = []

    for num in numbers:
        count[num] += 1

    for num in numbers:
        if count[num] <= threshold:
            result.append(num)
            count[num] = threshold + 1  # mark as processed

    return result