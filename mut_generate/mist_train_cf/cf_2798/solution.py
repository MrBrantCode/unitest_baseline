"""
QUESTION:
Implement a function `majorityElement(nums: List[int])` that finds the majority element in an array using the Boyer-Moore Voting Algorithm. The majority element is defined as the element that appears more than ⌊ n/3 ⌋ times in the array of size n, where n is the length of the input array. The function should return the majority element if it exists, otherwise return -1.
"""

from typing import List

def majorityElement(nums: List[int]) -> int:
    count1 = 0
    count2 = 0
    candidate1 = None
    candidate2 = None
    
    for num in nums:
        if count1 == 0:
            candidate1 = num
            count1 = 1
        elif num == candidate1:
            count1 += 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        elif num == candidate2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    
    count1 = 0
    count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    
    n = len(nums)
    if count1 > n // 3:
        return candidate1
    elif count2 > n // 3:
        return candidate2
    else:
        return -1