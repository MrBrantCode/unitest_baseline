"""
QUESTION:
Design a function `lengthOfLIS` that takes a list of integers `nums` as input and returns an integer representing the length of the longest increasing subsequence. The function should have a time complexity of O(n log n), where n is the length of the list.
"""

def lengthOfLIS(nums):
    n = len(nums)
    dp = [0] * n
    length = 0
    
    for num in nums:
        left, right = 0, length
        
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        dp[left] = num
        if left == length:
            length += 1
    
    return length