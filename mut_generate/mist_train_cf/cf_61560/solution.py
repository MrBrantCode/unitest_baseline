"""
QUESTION:
Write a function `get_positive_and_sort` that takes a list of integers as input, filters out non-positive numbers, and returns the remaining numbers sorted in ascending order. The function should not use the built-in `sort()` or `sorted()` functions. Instead, it should implement a custom sorting algorithm. Additionally, the function should include a helper function `swap_elements` to swap two elements in the list.
"""

def get_positive_and_sort(numbers: list):
    def swap_elements(n: list, index1: int, index2: int):
        temp = n[index1]
        n[index1] = n[index2]
        n[index2] = temp

    # Filter the list for positive numbers only
    numbers = [num for num in numbers if num > 0]

    # Implement bubble sort
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                swap_elements(numbers, j, j + 1)

    return numbers