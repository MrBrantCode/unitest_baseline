"""
QUESTION:
Create a function named `average_divisible_by_three` that takes an array of integers between -100 and 100, inclusive, and returns the average (rounded to the nearest whole number) of the positive numbers that are divisible by 3. If no such numbers exist, return -1.
"""

def average_divisible_by_three(arr):
    positive_nums = [num for num in arr if num > 0]
    divisible_nums = [num for num in positive_nums if num % 3 == 0]

    if len(divisible_nums) == 0:
        return -1

    average = sum(divisible_nums) / len(divisible_nums)
    return round(average)