"""
QUESTION:
Implement a function `src_number` that takes a list of integers as input. The function should return the source number, which is the number that appears only once in the input list, while all other numbers appear exactly twice. If no such number exists, return 0.
"""

from typing import List

def singleNumber(nums: List[int]) -> int:
    num_count = {}
    
    # Count the occurrences of each number in the input list
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    # Find the source number
    for num, count in num_count.items():
        if count == 1:
            return num
    
    # If no source number is found, return 0
    return 0