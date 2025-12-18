"""
QUESTION:
Write a recursive function `recursive_sum_product` that takes a list of integers as input and returns the sum and product of all elements in the list. If the list is empty, return None. If the list contains only one element, return that element as both the sum and product. For longer lists, divide the list into two halves, recursively find the sum and product of each half, and combine the results. Do not use built-in sum or product functions.
"""

def recursive_sum_product(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0], arr[0]
    else:
        mid = len(arr) // 2
        left_sum, left_product = recursive_sum_product(arr[:mid])
        right_sum, right_product = recursive_sum_product(arr[mid:])
        total_sum = left_sum + right_sum
        total_product = left_product * right_product
        return total_sum, total_product