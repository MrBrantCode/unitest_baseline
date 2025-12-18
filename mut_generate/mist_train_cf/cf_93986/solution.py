"""
QUESTION:
Write a recursive function named `sum_of_squares` that calculates the sum of squares of all even numbers in a given array of positive integers of length at most 100. The function should also return the count of odd numbers and a list of even numbers in the array, sorted in descending order. The recursion should be implemented such that the function calls itself with a smaller subarray in each recursive call.
"""

def sum_of_squares(arr):
    """
    Calculate the sum of squares of all even numbers in the given array, 
    count of odd numbers, and a list of even numbers in the array, 
    sorted in descending order.

    Args:
    arr (list): A list of positive integers.

    Returns:
    tuple: A tuple containing the sum of squares of even numbers, 
    the count of odd numbers, and a list of even numbers.
    """
    even_nums = []
    odd_count = 0

    if len(arr) == 0:
        return 0, 0, []

    if arr[0] % 2 == 0:
        even_nums.append(arr[0])
        even_sum = arr[0]**2
        odd_count = 0
    else:
        even_sum = 0
        odd_count = 1

    sub_even_sum, sub_odd_count, sub_even_nums = sum_of_squares(arr[1:])
    even_sum += sub_even_sum
    odd_count += sub_odd_count
    even_nums.extend(sub_even_nums)

    even_nums.sort(reverse=True)
    return even_sum, odd_count, even_nums