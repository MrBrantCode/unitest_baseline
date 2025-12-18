"""
QUESTION:
Given an array of length n containing integers from 1 to n inclusive, with exactly one integer duplicated and one integer missing, implement a function findErrorNums(nums) that returns a list containing the duplicated number followed by the missing number. The function takes in a list of integers nums and returns a list of integers.
"""

from typing import List

def findErrorNums(nums: List[int]) -> List[int]:
    n = len(nums)
    actual_sum = sum(nums)
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers

    actual_sum_set = sum(set(nums))
    duplicated_num = actual_sum - actual_sum_set 

    missing_num = expected_sum - actual_sum_set
    
    return [duplicated_num, missing_num]