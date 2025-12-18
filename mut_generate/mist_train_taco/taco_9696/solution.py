"""
QUESTION:
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 


Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""

def find_min_subarray_length(s: int, nums: list[int]) -> int:
    if not nums:
        return 0
    
    _min = float('inf')
    _sum = 0
    j = 0
    
    for i, n in enumerate(nums):
        _sum += n
        while _sum >= s:
            _min = min(i - j + 1, _min)
            _sum -= nums[j]
            j += 1
    
    return _min if _min != float('inf') else 0