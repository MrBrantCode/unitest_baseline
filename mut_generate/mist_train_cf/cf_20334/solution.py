"""
QUESTION:
Implement a function named `bubble_sort_descending` that takes a list of unique integers as input and returns the sorted list in descending order. The input list should contain at least 5 numbers and no more than 10 numbers, with each number within the range of 1 to 100. The function should use a custom sorting algorithm, not a built-in sorting function.
"""

def bubble_sort_descending(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers