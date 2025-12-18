"""
QUESTION:
Write a function `find_largest_palindrome` that takes an array of integers as input and returns the index of the largest palindromic number in the array. If there are multiple palindromic numbers with the same maximum length, return the index of the first occurrence. If there are no palindromic numbers in the array, return -1. The function should have a time complexity of O(n), where n is the length of the array, and should only use constant space.
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