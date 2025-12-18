"""
QUESTION:
Write a function `getNextGreaterElement` that takes an array `arr` of integers as input and returns an array of the same length. The function should return an array where each element at index `i` represents the next greater element of `arr[i]` in the input array. If there is no greater element for a particular element, the output array should have -1 at that index.
"""

from typing import List

def nextGreaterElements(nums1: List[int]) -> List[int]:
    stack = []
    result = [-1] * len(nums1)

    for i in range(len(nums1)):
        while stack and nums1[i] > nums1[stack[-1]]:
            result[stack.pop()] = nums1[i]
        stack.append(i)

    return result