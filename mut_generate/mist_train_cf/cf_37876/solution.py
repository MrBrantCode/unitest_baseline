"""
QUESTION:
Write a function `backtrack(nums, path)` that generates all possible permutations of the elements in `nums` using backtracking. The function should take two parameters: `nums`, a list of distinct integers, and `path`, a list representing the current permutation being constructed. It should return a list of lists, where each inner list represents a unique permutation of the elements in `nums`.
"""

from typing import List

def permute(nums: List[int], path: List[int]) -> List[List[int]]:
    result = []
    if len(path) == len(nums):
        result.append(path[:])  
        return result

    for num in nums:
        if num not in path:  
            path.append(num)  
            result += permute(nums, path)  
            path.pop()  

    return result