"""
QUESTION:
Write a function `sum_even_elements` that takes an array of integers as input, sums the first 5 even elements, and checks if the sum is greater than 10 and less than 20. The function should also count the number of even and odd elements in the array and return the sum, even count, and odd count. The input array is guaranteed to have 10 elements, where the first 5 elements are even numbers and the next 5 elements are odd numbers. Do not use built-in sum() function.
"""

def sum_even_elements(arr):
    """
    This function sums the first 5 even elements in the array, checks if the sum is greater than 10 and less than 20,
    and counts the number of even and odd elements in the array.

    Args:
        arr (list): An array of 10 integers, where the first 5 elements are even numbers and the next 5 elements are odd numbers.

    Returns:
        tuple: A tuple containing the sum of the first 5 even elements, the count of even elements, and the count of odd elements.
    """
    even_count = 0
    odd_count = 0
    total_sum = 0
    for i in range(len(arr)):
        if i < 5 and arr[i] % 2 == 0:
            total_sum += arr[i]
            even_count += 1
        elif i >= 5 and arr[i] % 2 != 0:
            odd_count += 1
    is_sum_in_range = "within" if 10 < total_sum < 20 else "not within"
    print(f"Sum is {total_sum} which is {is_sum_in_range} the range of 10 and 20")
    return total_sum, even_count, odd_count