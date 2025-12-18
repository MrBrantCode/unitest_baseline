"""
QUESTION:
Write a function `find_average` that calculates the average of a list of integers. The function must have a time complexity of O(n) and use only a constant amount of extra space.
"""

def find_average(nums):
    sum = 0
    count = 0

    for num in nums:
        sum += num
        count += 1

    average = sum / count

    return average