"""
QUESTION:
Write a function `find_largest_sum` that takes a list of integers as input and returns a tuple containing the largest sum of any three consecutive integers and the indices of the starting and ending elements of the subarray with the largest sum. The function should handle lists of length 3 or more.
"""

def find_largest_sum(nums):
    max_sum = float('-inf')
    start_index = 0
    end_index = 0

    for i in range(len(nums) - 2):
        curr_sum = nums[i] + nums[i+1] + nums[i+2]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start_index = i
            end_index = i + 2

    return (max_sum, [start_index, end_index])