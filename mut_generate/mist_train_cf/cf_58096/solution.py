"""
QUESTION:
Implement a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed while preserving the original order. The function should have a time complexity of O(n). It should count the occurrence frequency of each integer and exclude those that occur more than once.
"""

from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """Remove duplicates while maintaining order.
    Given a list of integers, remove any number that occurs more than once,
    while keeping the order of the remaining numbers the same as the original list.
    Determine the number of times each number occurs, and remove the numbers that occur more than once.
    """
    count_map = {}
    result = []
    for num in numbers:
        if num not in count_map:
            count_map[num] = 1
            result.append(num)
        else:
            count_map[num] += 1
            if count_map[num] > 1 and num in result:
                result.remove(num)
    return result