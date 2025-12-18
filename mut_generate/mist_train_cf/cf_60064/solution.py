"""
QUESTION:
Create a function named `get_positive_and_sort` that takes a list of integers as input, removes any non-positive integers and duplicates, sorts the remaining positive integers in ascending order, and returns them in a list. Implement a custom sorting algorithm using a helper function named `swap_elements` without using the built-in `sort()` or `sorted()` functions in Python.
"""

def get_positive_and_sort(numbers: list):
    """
    This function takes a list of integers, removes non-positive integers and duplicates, 
    sorts the remaining positive integers in ascending order, and returns them in a list.
    """

    def swap_elements(n: list, index1: int, index2: int):
        # Implemented helper function for swap elements for sorting
        temp = n[index1]
        n[index1] = n[index2]
        n[index2] = temp

    # List to store positive numbers
    positive_nums = []

    for num in numbers:
        # Adding positive numbers to the list
        if num > 0 and num not in positive_nums:
            positive_nums.append(num)

    # Implementing Bubble Sort to sort the elements in ascending order
    for i in range(len(positive_nums)):
        for j in range(len(positive_nums) - i - 1):
            if positive_nums[j] > positive_nums[j + 1]:
                swap_elements(positive_nums, j, j + 1)
    return positive_nums