"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of numbers as input, sorts the list in ascending order without using built-in sort functions, and returns the sorted list. The function should work for lists containing both integers and floating-point numbers.
"""

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers