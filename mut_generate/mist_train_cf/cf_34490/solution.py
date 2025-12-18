"""
QUESTION:
Write a function `findUniqueElement` that takes a list of integers as input, where every element appears twice except for one. The function should return the integer that appears only once. The input list will always have exactly one element that appears only once, while all other elements appear twice.
"""

def findUniqueElement(nums):
    unique_element = 0
    for num in nums:
        unique_element ^= num
    return unique_element