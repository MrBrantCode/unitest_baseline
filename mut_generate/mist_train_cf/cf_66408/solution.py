"""
QUESTION:
Remove all non-consecutive duplicate elements from a list of integers while preserving the original order and allowing for optional consecutive duplicates. The function should have a time complexity of O(n) and be able to handle empty lists. The function should have the following signature: `remove_duplicates(numbers: List[int], allow_consecutive_duplicates: bool = True) -> List[int]`.
"""

from typing import List

def remove_duplicates(numbers: List[int], allow_consecutive_duplicates: bool = True) -> List[int]:
    if len(numbers) == 0:
        return []
       
    if allow_consecutive_duplicates:
        new_length = 1
        for i in range(1,len(numbers)):
            if numbers[i] != numbers[new_length-1]:
                numbers[new_length] = numbers[i]
                new_length += 1        
    else:
        seen = set()
        new_length = 0
        for i in range(len(numbers)):
            if numbers[i] not in seen:
                seen.add(numbers[i])
                numbers[new_length] = numbers[i]
                new_length += 1

    return numbers[:new_length]