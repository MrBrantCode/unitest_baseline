"""
QUESTION:
Create a function `advanced_sort_by_digit_product` that takes an array of positive integers as input. The function should return the sorted array in descending order based on the product of the digits of each number. If two numbers have the same product of digits, they should be sorted in descending order based on the sum of their digits. If the sum of digits is also the same, the numbers should be sorted in ascending order of their numerical value.
"""

def advanced_sort_by_digit_product(arr):
    def digit_product(num):
        product = 1
        for digit in str(num):
            product *= int(digit)
        return product

    def digit_sum(num):
        return sum(int(digit) for digit in str(num))

    return sorted(arr, key=lambda num: (-digit_product(num), -digit_sum(num), num))