"""
QUESTION:
Write a function `partition_list(nums)` that takes a list of positive integers `nums` as input and partitions the list into two non-empty parts such that the sum of the elements in the first part is greater than or equal to twice the sum of the elements in the second part, and the difference between the sums of the two parts is minimized.
"""

def partition_list(nums):
    total_sum = sum(nums)
    current_sum = 0
    min_diff = float('inf')
    partition_index = -1

    for i in range(len(nums)):
        current_sum += nums[i]
        remaining_sum = total_sum - current_sum
        diff = abs(current_sum - 2 * remaining_sum)
        
        if diff < min_diff and current_sum >= 2 * remaining_sum:
            min_diff = diff
            partition_index = i

    return nums[:partition_index+1], nums[partition_index+1:]