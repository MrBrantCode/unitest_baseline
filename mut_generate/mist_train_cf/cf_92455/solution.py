"""
QUESTION:
Write a function `filter_and_sort(arr)` that takes an array of integers as input and returns a tuple containing the array with all even numbers removed and the remaining odd numbers sorted in descending order, as well as the sum of the remaining odd numbers. The function should have a time complexity of O(nlogn) or better.
"""

def filter_and_sort(arr):
    # Filter out even numbers
    filtered_arr = [num for num in arr if num % 2 != 0]

    # Sort the remaining odd numbers in descending order
    sorted_arr = sorted(filtered_arr, reverse=True)

    # Calculate the sum of the remaining odd numbers
    sum_odd_numbers = sum(sorted_arr)

    return sorted_arr, sum_odd_numbers