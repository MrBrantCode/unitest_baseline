"""
QUESTION:
Write a function named `max_sublist_sum` that takes a list of integers as input and returns a tuple containing the maximum sum of the most substantial continuous sublist, and its start and end indices. If the input list is empty, the function should return `None`. The function should assume that the list is at least one element long and use 0-based indices. In case of a tie, the function should return the indices of the first sublist with the maximum sum.
"""

def entrance(nums):
    if len(nums) == 0:
        return None
  
    max_sum = current_sum = nums[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if current_sum <= 0:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return (max_sum, start, end)