"""
QUESTION:
Write a function named `custom_sort` that sorts a list of numbers in descending order without using any built-in or commonly used sorting algorithms or external libraries. The function should return the sorted list. The input list contains only integers.
"""

def custom_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers