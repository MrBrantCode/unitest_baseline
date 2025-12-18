"""
QUESTION:
Write a recursive function named `cumulative_product` that takes an array of numbers and outputs each element along with its cumulative product. The function should handle arrays of any length, including empty arrays, and accommodate zero, negative, and positive numbers. The function should use recursion and print the individual elements and their corresponding cumulative products.
"""

def cumulative_product(arr, i = 0, product = 1):
    if i == len(arr):
        return
    else:
        product *= arr[i]
        print('Element:', arr[i], ', Cumulative Product:', product)
        cumulative_product(arr, i + 1, product)