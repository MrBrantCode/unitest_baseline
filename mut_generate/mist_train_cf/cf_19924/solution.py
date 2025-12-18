"""
QUESTION:
Write a function `find_numbers(n)` that returns a list of numbers from 1 to `n` (inclusive) that meet the following conditions: the number is divisible by 6, the sum of its digits is divisible by 3, and the number is not divisible by 4.
"""

def find_numbers(n):
    def is_divisible_by_6(num):
        return num % 6 == 0

    def is_sum_of_digits_divisible_by_3(num):
        return sum(int(digit) for digit in str(num)) % 3 == 0

    def is_not_divisible_by_4(num):
        return num % 4 != 0

    numbers = []
    for num in range(1, n+1):
        if is_divisible_by_6(num) and is_sum_of_digits_divisible_by_3(num) and is_not_divisible_by_4(num):
            numbers.append(num)
    return numbers