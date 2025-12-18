"""
QUESTION:
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:


Input: [3,2,3]
Output: [3]

Example 2:


Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

def find_majority_elements(nums):
    if not nums:
        return []
    
    dct = {}
    for el in nums:
        if el in dct:
            dct[el] += 1
        else:
            dct[el] = 1
    
    fin = []
    for key in dct:
        if dct[key] > len(nums) // 3:
            fin.append(key)
    
    return fin