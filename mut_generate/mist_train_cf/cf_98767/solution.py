"""
QUESTION:
Create a function called `list_product_sum_diff` that takes two lists, A and B, as input. List A contains odd numbers ranging from 3 to 9, and list B contains even numbers ranging from 1 to 10, both inclusive. The function should return the product of the sum of all elements in A and B, and the difference between the maximum and minimum values in the combined list of A and B.
"""

def list_product_sum_diff(A, B):
    sum_ab = sum(A) + sum(B)
    diff_ab = max(A+B) - min(A+B)
    product = sum_ab * diff_ab
    return product