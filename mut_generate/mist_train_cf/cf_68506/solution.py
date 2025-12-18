"""
QUESTION:
Implement a function `sort_by_digit_product(arr)` that takes a list of positive integers as input and returns a new list sorted in descending order based on the product of the digits of each number. If two numbers have the same product of digits, they should be sorted by the sum of their digits in descending order, and if the sum is also equal, they should be sorted in ascending numerical order.
"""

def sort_by_digit_product(arr):
    """
    Sort an array of positive integers primarily based on the product 
    of their digits. If the product is similar, sort them based on the 
    sum of the digits and if the sum is also equal, arrange them in 
    ascending order.

    Args:
    arr (list): A list of positive integers.

    Returns:
    list: The list sorted based on the criteria.
    """
    def digit_product_sum(n):
        product = 1
        digit_sum = 0
        for digit in str(n):
            product *= int(digit)
            digit_sum += int(digit)
        return product, digit_sum, n

    arr = sorted(arr, key=digit_product_sum, reverse=True)

    return arr