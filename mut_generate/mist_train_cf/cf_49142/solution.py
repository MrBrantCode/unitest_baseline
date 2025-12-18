"""
QUESTION:
Design a recursive function `product_of_sums(lst, target, product=1, index=0)` that calculates the product of the sum of consecutive tuples' elements in a list until reaching a specified limit. The function should handle exceptions such as an empty list, non-numeric elements in tuples, or tuples containing more than two elements.
"""

def product_of_sums(lst, target, product=1, index=0):
    if not lst:
        return "Error: List is empty"
    if index == len(lst):
        return product
    if not isinstance(lst[index], tuple) or len(lst[index]) != 2:
        return f"Error: Element at index {index} is not a tuple of two numbers"
    if not all(isinstance(x, (int, float)) for x in lst[index]):
        return f"Error: Tuple at index {index} contains non-numeric elements"
    new_product = product * sum(lst[index])
    if new_product > target:
        return product
    else:
        return product_of_sums(lst, target, new_product, index + 1)