"""
QUESTION:
Write a function called `product_except_self` that takes an array of numbers and returns an array whose elements are the product of all the elements except the element at the current index. You are not allowed to use division in your solution. The function should take one argument: an array of numbers and return an array of numbers.
"""

def product_except_self(arr):
    n = len(arr)
    left_products = [1] * n
    right_products = [1] * n
    output = [1] * n

    for i in range(1, n):
        left_products[i] = left_products[i-1] * arr[i-1]

    for i in range(n-2, -1, -1):
        right_products[i] = right_products[i+1] * arr[i+1]

    for i in range(n):
        output[i] = left_products[i] * right_products[i]

    return output