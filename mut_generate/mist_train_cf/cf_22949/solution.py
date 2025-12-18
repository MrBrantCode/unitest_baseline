"""
QUESTION:
Write a function `cumulative_sum(numbers)` that takes a list of numbers as input and returns a list containing the cumulative sum of the positive numbers in the input list, excluding any numbers that are divisible by 3, in descending order.
"""

def cumulative_sum(numbers):
    positive_numbers = [num for num in numbers if num > 0]  # Filter out negative numbers
    positive_numbers = [num for num in positive_numbers if num % 3 != 0]  # Filter out numbers divisible by 3
    cumulative_sum = []
    current_sum = 0
    for num in sorted(positive_numbers, reverse=True):  # Sort positive numbers in descending order
        current_sum += num
        cumulative_sum.append(current_sum)
    return cumulative_sum