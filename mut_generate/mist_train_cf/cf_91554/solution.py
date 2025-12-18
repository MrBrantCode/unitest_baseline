"""
QUESTION:
Implement the `majorityElement` function that finds the majority element in an array of integers using the Boyer-Moore Voting Algorithm. The majority element is the element that appears more than ⌊ n/2 ⌋ times in the array of size n. Assume the majority element always exists in the given array.

The function should take a list of integers `nums` as input and return the majority element. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

from typing import List

def majorityElement(nums: List[int]) -> int:
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate