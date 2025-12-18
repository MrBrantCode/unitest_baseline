"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers as input and returns a list of integers with all duplicates removed. The function should maintain the order of the remaining elements identical to the input, achieve a time complexity of O(n), and a space complexity of O(1) without creating any additional collections.
"""

from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    if not numbers: 
        return []
    
    numbers.sort()
    write_index = 1
    for read_index in range(1, len(numbers)):
        if numbers[read_index] != numbers[write_index-1]:
            numbers[write_index] = numbers[read_index]
            write_index += 1
    
    return numbers[:write_index]