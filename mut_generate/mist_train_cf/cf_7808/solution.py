"""
QUESTION:
Write a function named `find_longest_substring` that takes a list of positive integers as input and returns the longest common substring. The substring should consist of consecutive integers in the list, the characters in the substring should be in strictly increasing order, and the length of the substring should be greater than or equal to 3. If there are multiple substrings that meet this criteria and have the same maximum length, return the substring that occurs first in the list.
"""

def find_longest_substring(nums):
    start = 0
    end = 0
    max_length = 0
    longest_substring = []

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            end = i
        else:
            if max_length < end - start + 1 >= 3:
                max_length = end - start + 1
                longest_substring = nums[start:end+1]
            start = i
            end = i

    # Check if the last substring is the longest
    if max_length < end - start + 1 >= 3:
        max_length = end - start + 1
        longest_substring = nums[start:end+1]

    return longest_substring