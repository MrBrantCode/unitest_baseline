"""
QUESTION:
Create a function `sum_of_digits` that takes a list of integers as input and returns the sum of all their digits. The function should handle negative integers, zeros, and integers with only one digit, and should not use any built-in functions or libraries for arithmetic operations or string manipulations. The time complexity of the function should be O(log n), where n is the maximum value among the given integers.
"""

def sum_of_digits(numbers):
    total_sum = 0
    for num in numbers:
        abs_num = abs(num)
        while abs_num != 0:
            total_sum += abs_num % 10
            abs_num //= 10
    return total_sum