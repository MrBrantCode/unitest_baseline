"""
QUESTION:
Implement a function named `sort_descending` that takes a list of integers as input and returns the sorted list in descending order without using any built-in sorting functions or methods.
"""

def sort_descending(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers