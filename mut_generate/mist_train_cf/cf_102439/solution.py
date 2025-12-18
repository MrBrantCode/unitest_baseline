"""
QUESTION:
Develop a function called `filter_and_sum` that takes a list of numbers as input. The function should filter out numbers that are divisible by both 2 and 3 and contain the digit 5, then return the sum of the remaining numbers in the list.
"""

def filter_and_sum(numbers):
    return sum(num for num in numbers if not (num % 2 == 0 and num % 3 == 0 and '5' in str(num)))