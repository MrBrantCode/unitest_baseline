"""
QUESTION:
Write a function called calculate_average that takes a list of numbers as input and returns the average of those numbers. The function must manually calculate the sum and average without using any built-in functions or libraries. The input list may contain duplicate numbers.
"""

def calculate_average(nums):
    total = 0
    count = 0
    for num in nums:
        total += num
        count += 1
    average = total / count
    return average