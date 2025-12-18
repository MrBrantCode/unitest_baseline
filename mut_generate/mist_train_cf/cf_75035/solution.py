"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of integers and an integer threshold as input, and returns a new list containing the elements from the input list that occur at most `threshold` times. The function must preserve the original order of elements and have a time complexity of O(n).
"""

from typing import List
from collections import defaultdict

def remove_duplicates(numbers: List[int], threshold: int) -> List[int]:
    counts = defaultdict(int)
    result = []

    for num in numbers:
        counts[num] += 1
        if counts[num] <= threshold:
            result.append(num)
    
    return result