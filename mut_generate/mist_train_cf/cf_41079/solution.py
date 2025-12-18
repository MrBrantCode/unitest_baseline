"""
QUESTION:
Implement a function `count_frequency` that takes a list of integers `nums` as input and returns a dictionary with integers as keys and their frequencies in the list as values.
"""

def count_frequency(nums):
    frequency_dict = {}
    for num in nums:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    return frequency_dict