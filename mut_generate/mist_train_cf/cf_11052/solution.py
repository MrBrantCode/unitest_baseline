"""
QUESTION:
Implement a function called `sort_array` that takes an array of integers as input and returns a sorted array. The sorted array should have the following properties: it should be sorted in ascending order, and even numbers should come before odd numbers. You cannot use any built-in sorting functions or libraries.
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