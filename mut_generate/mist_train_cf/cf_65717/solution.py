"""
QUESTION:
Create a function called `calculate_frequency` that generates a dictionary of unique entities paired with their total occurrences in a given numerical list. The function should handle a large numerical list with millions of elements efficiently.
"""

def calculate_frequency(nums):
    frequency_dict = {}
    for num in nums:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1
    return frequency_dict