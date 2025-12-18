"""
QUESTION:
Write a recursive function `check_parity_of_sum` that takes an integer as input and returns 'even' if the sum of its digits is even, and 'odd' if the sum is odd, without using standard library methods for number to string conversion.
"""

def check_parity_of_sum(num):
    def sum_of_digits(num):
        if num == 0:
            return 0
        else:
            return num % 10 + sum_of_digits(num // 10)

    total = sum_of_digits(num)
    if total % 2 == 0:
        return 'even'
    else:
        return 'odd'