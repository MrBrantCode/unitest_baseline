"""
QUESTION:
Create a function named `divisible_by_5_and_7` that takes a list of positive integers as input. The function should return two values: a list of unique elements from the input list that are divisible by both 5 and 7, sorted in ascending order, and the count of these unique elements.
"""

def divisible_by_5_and_7(numbers):
    result = [num for num in set(numbers) if num % 5 == 0 and num % 7 == 0]
    result.sort()
    return result, len(result)