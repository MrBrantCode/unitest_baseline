"""
QUESTION:
Write a function `group_ranges` that takes a list of integers as input, groups the numbers into continuous ranges where each number is exactly one greater than the previous number, and returns a list of lists where each sublist contains the range of numbers and their sum. The input list can contain duplicate numbers, and the output should not include any duplicates.
"""

def group_ranges(nums):
    ranges = []
    nums.sort()
    start = nums[0]
    total_sum = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            total_sum += nums[i]
        else:
            ranges.append(list(range(start, nums[i-1]+1)))
            ranges.append(total_sum)
            start = nums[i]
            total_sum = nums[i]
    
    ranges.append(list(range(start, nums[-1]+1)))
    ranges.append(total_sum)
    
    return ranges