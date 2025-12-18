"""
QUESTION:
Implement a function named `sort_negative_numbers` that takes a list of numbers as input, extracts the negative numbers, and returns them in a new list sorted in ascending order. The function must implement its own sorting algorithm without using any built-in sorting functions or libraries, and it should have a time complexity of O(n^2).
"""

def sort_negative_numbers(lst):
    negative_nums = [num for num in lst if num < 0]  # Get all negative numbers
    n = len(negative_nums)

    # Implement Bubble Sort algorithm
    for i in range(n - 1):
        for j in range(n - i - 1):
            if negative_nums[j] > negative_nums[j + 1]:
                negative_nums[j], negative_nums[j + 1] = negative_nums[j + 1], negative_nums[j]

    return negative_nums