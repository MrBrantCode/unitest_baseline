"""
QUESTION:
Write a function `group_three` that takes a list of numbers as input and returns a list of sublists, where each sublist contains at most three consecutive numbers from the original list. If the length of the input list is not a multiple of three, the last sublist should contain the remaining numbers. The input list is not guaranteed to be non-empty or contain only integers.
"""

def group_three(nums): 
    result = []
    nums_length = len(nums)

    for index in range(0, nums_length, 3):
        result.append(nums[index:index + 3])

    return result