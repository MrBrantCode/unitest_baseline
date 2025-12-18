"""
QUESTION:
Write a function `find_largest_palindrome(nums)` that finds the index of the largest palindromic number in the given array `nums`. If there are multiple palindromic numbers with the same maximum length, return the index of the first occurrence. If there are no palindromic numbers in the array, return -1. The function must have a time complexity of O(n), where n is the length of the array, and must be implemented using only constant space, without using additional data structures.
"""

def find_largest_palindrome(nums):
    max_length = 0
    max_index = -1
    
    for i in range(len(nums)):
        if str(nums[i]) == str(nums[i])[::-1]:
            if len(str(nums[i])) > max_length:
                max_length = len(str(nums[i]))
                max_index = i
    
    return max_index