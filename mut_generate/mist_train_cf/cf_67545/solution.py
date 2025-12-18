"""
QUESTION:
Implement a function `get_positive_and_sort(numbers)` that takes a list of integers as input, filters out non-positive integers and duplicates, and returns the remaining positive integers in ascending order without using the built-in `sort()` or `sorted()` functions. Additionally, create a helper function `swap_elements(numbers, index1, index2)` that swaps the elements at the specified indices in the list. The sorting algorithm should be implemented exclusively within the `swap_elements` function.
"""

def get_positive_and_sort(numbers: list):
    def swap_elements(numbers: list, index1: int, index2: int):
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

    positive_nums = [num for num in set(numbers) if num > 0]

    for i in range(len(positive_nums)):
        for j in range(i + 1, len(positive_nums)):
            if positive_nums[i] > positive_nums[j]:
                swap_elements(positive_nums, i, j)

    return positive_nums