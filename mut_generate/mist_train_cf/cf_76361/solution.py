"""
QUESTION:
Create a function named `unique_and_frequency` that takes a list of integers as input, which can contain duplicates. The function should return two outputs: a list of unique numbers in descending order (without using Python's built-in sorting functions) and a dictionary mapping each unique number to its frequency in the original list (without using the `count` dictionary function).
"""

def unique_and_frequency(nums):
    # remove duplicates
    unique_nums = list(set(nums))

    # bubble sort in descending order
    for i in range(len(unique_nums)):
        for j in range(0, len(unique_nums) - i - 1):
            if unique_nums[j] < unique_nums[j + 1] :
                unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]

    # create frequency dictionary
    frequency_dict = {}
    for num in unique_nums:
        count = 0
        for i in nums:
            if i == num:
                count += 1
        frequency_dict[num] = count

    return unique_nums, frequency_dict