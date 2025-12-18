"""
QUESTION:
Write a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the numbers that occur exactly twice in the input list. Also, write a function `greater_than_average` that takes a list of integers as input, calculates the average of the list, and returns a new list containing only the numbers that are greater than the average. The input list will contain 20 random integers between 1 and 1000.
"""

def remove_duplicates(numbers):
    duplicates = []
    unique_numbers = set(numbers)
    for num in unique_numbers:
        if numbers.count(num) == 2:
            duplicates.append(num)
    return duplicates

def greater_than_average(numbers):
    average = sum(numbers) / len(numbers)
    return [num for num in numbers if num > average]