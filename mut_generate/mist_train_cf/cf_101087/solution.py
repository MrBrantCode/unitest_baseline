"""
QUESTION:
Create a function called `list_product_sum_diff` that takes two lists `A` and `B` as input. The function should calculate the sum of all elements in both lists, find the difference between the maximum and minimum values in both lists, and return the product of these two values. The function should work for any two lists of integers.
"""

def list_product_sum_diff(A, B):
    sum_ab = sum(A) + sum(B)
    diff_ab = max(A+B) - min(A+B)
    product = sum_ab * diff_ab
    return product