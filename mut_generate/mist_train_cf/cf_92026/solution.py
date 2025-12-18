"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of numbers as input and returns a tuple containing the sorted list in ascending order, the total number of comparisons performed, and the total number of swaps performed. The function should use the Bubble Sort algorithm.
"""

def bubble_sort(numbers):
    comparisons = 0
    swaps = 0
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swaps += 1
    return tuple(numbers), comparisons, swaps