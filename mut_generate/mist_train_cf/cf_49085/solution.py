"""
QUESTION:
Write a function named `bubble_sort` that sorts a list of numbers in ascending order using the bubble sort algorithm. The function should take a list of numbers as input and return the sorted list.
"""

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]: # Swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers