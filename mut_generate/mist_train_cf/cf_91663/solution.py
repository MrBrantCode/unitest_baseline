"""
QUESTION:
Create a function named `sort_array` that takes an array of integers as input and returns the sorted array. The array should be sorted such that the even numbers come before the odd numbers, and within each group, the numbers should be in ascending order. The function should not use any built-in sorting functions or libraries.
"""

def sort_array(arr):
    even_nums = []
    odd_nums = []

    # Separate even and odd numbers
    for num in arr:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)

    # Sort even and odd numbers
    even_nums.sort()
    odd_nums.sort()

    # Concatenate even and odd numbers
    sorted_arr = even_nums + odd_nums

    return sorted_arr