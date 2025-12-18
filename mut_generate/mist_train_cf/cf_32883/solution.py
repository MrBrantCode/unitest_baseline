"""
QUESTION:
Write a function `sum_of_digits_in_product` that takes two positive integers `num1` and `num2` as input and returns the sum of the digits in the product `num1 * num2`. Assume that the input integers `num1` and `num2` can be very large and may not fit into the standard integer data types.
"""

def sum_of_digits_in_product(num1, num2):
    product = num1 * num2
    digit_sum = 0
    product_str = str(product)
    for digit in product_str:
        digit_sum += int(digit)
    return digit_sum