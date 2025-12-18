"""
QUESTION:
Write a function named `insert_zeros` that takes a list of integers as input and returns a new list with zeros inserted after every 4 elements. The input list contains single-digit numbers.
"""

def insert_zeros(nums):
    output = []
    for i in range(len(nums)):
        output.append(nums[i])
        if (i+1) % 4 == 0:
            output.append(0)
    return output