"""
QUESTION:
Write a function `calculate_mean_median(numbers)` that calculates the mean and median of a given list of numbers. The function should sort the list first, then calculate the mean by summing up all numbers in the list and dividing by the length of the list. If the length of the list is an odd number, the median is the middle number. If the length of the list is an even number, the median is the average of the two middle numbers.
"""

def calculate_mean_median(numbers):
    numbers.sort()
    mean = sum(numbers) / len(numbers)
    if len(numbers) % 2 == 1:
        median = numbers[len(numbers) // 2]
    else:
        median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    return mean, median