"""
QUESTION:
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


Example 1:


Input: nums = [1,2,3,1], k = 3
Output: true



Example 2:


Input: nums = [1,0,1,1], k = 1
Output: true



Example 3:


Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

def contains_nearby_duplicate(nums, k):
    # Create a dictionary to store the most recent index of each number
    index_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Check if the number is already in the dictionary
        if num in index_map:
            # Check if the difference between the current index and the last seen index is at most k
            if i - index_map[num] <= k:
                return True
        # Update the most recent index of the number
        index_map[num] = i
    
    # If no such pair is found, return False
    return False