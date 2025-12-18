"""
QUESTION:
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:


Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note: 


       There may be more than one LIS combination, it is only necessary for you to return the length.
       Your algorithm should run in O(n2) complexity.


Follow up: Could you improve it to O(n log n) time complexity?
"""

def longest_increasing_subsequence_length(nums):
    if len(nums) == 0:
        return 0
    
    res = [nums[0]]

    def binary_search(l, target):
        left, right = 0, len(l) - 1
        while left < right:
            mid = (left + right) // 2
            if l[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
    
    for i in range(1, len(nums)):
        if nums[i] > res[-1]:
            res.append(nums[i])
        else:
            res[binary_search(res, nums[i])] = nums[i]
    
    return len(res)