"""
QUESTION:
Write a function named `sort_descending` that takes a list of numbers as input and returns the list sorted in descending order without using any built-in sorting functions.
"""

def sort_descending(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers