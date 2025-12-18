"""
QUESTION:
Write a function named `cumulative_sum` that takes a list of numbers as input. The function should return a list containing the cumulative sum of all positive numbers in the input list, excluding any numbers divisible by 3, in descending order.
"""

def cumulative_sum(numbers):
    positive_numbers = [num for num in numbers if num > 0 and num % 3 != 0]
    current_sum = 0
    return sorted([current_sum := current_sum + num for num in sorted(positive_numbers, reverse=True)], reverse=True)