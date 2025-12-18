"""
QUESTION:
Create a function named `count_unique` that takes a list of integers as input and returns a dictionary containing the count of each unique integer in the input list. The function should handle empty input lists and return an empty dictionary in such cases. The input is a list of integers and the output is a dictionary where the keys are the unique integers from the input list and the values are their corresponding counts.
"""

from typing import List, Dict

def count_unique(nums: List[int]) -> Dict[int, int]:
    unique_counts = {}
    for num in nums:
        if num in unique_counts:
            unique_counts[num] += 1
        else:
            unique_counts[num] = 1
    return unique_counts