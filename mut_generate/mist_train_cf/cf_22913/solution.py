"""
QUESTION:
Write a function `product_of_elements` that takes an array of numbers as input and returns an array whose elements are the product of all the elements in the input array except the element at the current index. The function must not use division or any built-in multiplication functions in its solution. The input array is expected to have at least two elements.
"""

def product_of_elements(arr):
    n = len(arr)
    if n < 2:
        return []

    left_products = [1] * n
    for i in range(1, n):
        left_products[i] = left_products[i-1] * arr[i-1]

    right_products = [1] * n
    for i in range(n-2, -1, -1):
        right_products[i] = right_products[i+1] * arr[i+1]

    result = [1] * n
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result