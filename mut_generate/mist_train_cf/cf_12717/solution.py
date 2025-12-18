"""
QUESTION:
Create a function named `filter_and_sort` that takes an array of integers as input and returns a tuple containing a sorted array of odd numbers in descending order and their sum. The function should have a time complexity of O(nlogn) or better.
"""

def filter_and_sort(arr):
    # Filter out even numbers and sort the remaining odd numbers in descending order
    sorted_arr = sorted([num for num in arr if num % 2 != 0], reverse=True)

    # Calculate the sum of the remaining odd numbers
    sum_odd_numbers = sum(sorted_arr)

    return sorted_arr, sum_odd_numbers