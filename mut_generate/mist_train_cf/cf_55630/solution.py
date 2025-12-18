"""
QUESTION:
Implement a function `bubble_sort` that takes a list of integers as input and returns the sorted list using an optimized version of the Bubble Sort algorithm. The function should also validate the input, returning an error message if the input is not a list of integers. The function should handle edge cases, such as single-element lists, empty lists, and lists with negative integers.
"""

def bubble_sort(numbers):
    if not isinstance(numbers, list):
        return "Input should be a list of integers"
    for num in numbers:
        if not isinstance(num, int):
            return "Input should be a list of integers"

    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers