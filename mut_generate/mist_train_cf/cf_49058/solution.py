"""
QUESTION:
Write a function named `manipulate_array` that takes an array of 3 numbers and returns the result of the following operations: multiply the array by its sum, subtract the product of the first two elements, and finally return the result modulo 10000007.
"""

def manipulate_array(arr):
    sum_of_elements = sum(arr)
    product_of_first_two = arr[0] * arr[1]
    result = (sum_of_elements * product_of_first_two) - product_of_first_two
    result %= 10000007
    return result