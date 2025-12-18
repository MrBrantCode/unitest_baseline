"""
QUESTION:
Create a function `find_recurring_nums` that takes a list of integers as input and returns a dictionary where the keys are the recurring numbers in the list and their corresponding values are the frequencies of these numbers. The dictionary should preserve the order of first appearance of the recurring elements in the list. The function should have a time complexity better than O(n^2).
"""

def find_recurring_nums(nums):
    num_frequency = {}
    for num in nums:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1

    return {k: v for k, v in num_frequency.items() if v > 1}