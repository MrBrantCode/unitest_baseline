"""
QUESTION:
Write a function named `bubble_sort` that sorts a list of numbers in ascending order. The function should take a list of numbers as input and return the sorted list. Implement the bubble sort algorithm.
"""

def bubble_sort(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return numbers