"""
QUESTION:
Write a recursive function called `sort_numbers` that sorts a list of integers in descending order. The function should take a list of integers as input, and return a new list containing the same integers sorted in descending order. Do not use any built-in sorting functions or nested loops.
"""

def sort_numbers(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        less = [x for x in numbers[1:] if x <= pivot]
        greater = [x for x in numbers[1:] if x > pivot]
        return sort_numbers(greater) + [pivot] + sort_numbers(less)