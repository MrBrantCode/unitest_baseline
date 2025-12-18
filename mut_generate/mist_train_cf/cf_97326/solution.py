"""
QUESTION:
Write a function named `product_of_elements` that takes an array of numbers as input and returns an array where each element is the product of all numbers in the input array except the number at the same index. Do not use division or any built-in multiplication functions in the solution. The input array is guaranteed to contain at least two elements.
"""

def product_of_elements(arr):
    n = len(arr)
    if n < 2:
        return []

    # Create an array to store the product of elements before the current index
    left_products = [1] * n
    for i in range(1, n):
        left_products[i] = left_products[i-1] * arr[i-1]

    # Create an array to store the product of elements after the current index
    right_products = [1] * n
    for i in range(n-2, -1, -1):
        right_products[i] = right_products[i+1] * arr[i+1]

    # Multiply the corresponding elements from both arrays to get the final result
    result = [1] * n
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result