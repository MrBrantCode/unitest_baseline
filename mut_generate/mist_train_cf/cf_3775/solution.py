"""
QUESTION:
Write a function `sort_descending` that takes a list of numbers as input and returns the list sorted in descending order without using any built-in sorting functions. The function should have a time complexity of O(n^2) and should not use any external libraries.
"""

def sort_descending(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers