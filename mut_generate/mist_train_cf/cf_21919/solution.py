"""
QUESTION:
Create a function `sum_of_products(number)` that calculates the sum of the products of the odd digits of a given number with its reverse. If there are no odd digits in the number, return -1. The input number will not exceed 10^9 and will have at least 3 digits.
"""

def sum_of_products(number):
    number_str = str(number)
    reverse_number = number_str[::-1]
    product_sum = 0

    has_odd_digit = False
    for i in range(len(number_str)):
        digit = int(number_str[i])
        if digit % 2 != 0:
            has_odd_digit = True
            reverse_digit = int(reverse_number[i])
            product_sum += digit * reverse_digit

    if has_odd_digit:
        return product_sum
    else:
        return -1