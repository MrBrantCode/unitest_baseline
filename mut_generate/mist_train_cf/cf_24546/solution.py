"""
QUESTION:
Create a function named `find_avg` that calculates the average of a list of numbers. The function should take a list of numbers as input, and return the average value. The function must use a loop to iterate over the input list.
"""

def find_avg(nums):
    total = 0
    for num in nums:
        total += num

    return total / len(nums)