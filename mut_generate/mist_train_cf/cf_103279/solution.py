"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of numbers as input, sorts the list in ascending order using the Bubble Sort algorithm, and returns the sorted list along with the total number of comparisons and swaps performed during the sorting process.
"""

def entance(numbers):
    comparisons = 0
    swaps = 0
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swaps += 1
    return numbers, comparisons, swaps