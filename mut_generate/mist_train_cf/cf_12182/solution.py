"""
QUESTION:
Write a function named `find_average_even` that calculates the average of all the even numbers in a given array of integers without using built-in functions or libraries. The array can contain up to 10^6 positive or negative integers in any order. The function should return 0 if no even numbers are found.
"""

def find_average_even(arr):
    """
    Calculate the average of all even numbers in the given array.

    Args:
    arr (list): A list of integers.

    Returns:
    float: The average of all even numbers in the array. Returns 0 if no even numbers are found.
    """
    sum_even = 0
    count_even = 0

    for num in arr:
        if num % 2 == 0:
            sum_even += num
            count_even += 1

    if count_even > 0:
        return sum_even / count_even
    else:
        return 0