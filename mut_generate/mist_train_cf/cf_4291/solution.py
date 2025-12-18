"""
QUESTION:
Write a function `group_and_sort(numbers)` that takes a list of positive integers as input, removes duplicates, groups the numbers by their last digit, and returns a list of lists where each inner list contains the numbers with the same last digit in ascending order. The function should return a list of 10 inner lists, one for each possible last digit (0-9), even if there are no numbers with that last digit in the input.
"""

def group_and_sort(numbers):
    numbers = list(set(numbers))  # Remove duplicates from the list
    groups = [[] for _ in range(10)]  # Create a list of 10 empty lists for each digit

    for num in numbers:
        last_digit = num % 10
        groups[last_digit].append(num)

    for i in range(10):
        groups[i].sort()  # Sort each group in ascending order

    return groups