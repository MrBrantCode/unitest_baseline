"""
QUESTION:
Create a function `second_largest_index` that takes a list of at least two positive integers as input. The function should return the index of the second largest number in the list, with the condition that the second largest number must not be a duplicate.
"""

def second_largest_index(nums):
    largest = second_largest = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[largest]:
            second_largest = largest
            largest = i
        elif nums[i] > nums[second_largest] and nums[i] != nums[largest]:
            second_largest = i

    return second_largest