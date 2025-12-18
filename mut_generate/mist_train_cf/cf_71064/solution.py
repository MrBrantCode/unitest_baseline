"""
QUESTION:
Write a function `five_nine_twelve(n)` that takes an integer `n` as input and returns the cumulative count of integers from 1 to `n` that contain the digit 5, are divisible by either 9 or 12, and have a digit sum that is a multiple of 3.
"""

def five_nine_twelve(n: int) -> int:
    def has_five(num: int) -> bool:
        return '5' in str(num)

    def is_fully_divisible(num: int) -> bool:
        return num % 9 == 0 or num % 12 == 0

    def sum_of_digits(num: int) -> int:
        return sum(int(digit) for digit in str(num))

    def sum_is_multiply_of_three(num: int) -> bool:
        return sum_of_digits(num) % 3 == 0

    count = 0
    for i in range(1, n+1):
        if has_five(i) and is_fully_divisible(i) and sum_is_multiply_of_three(i):
            count += 1
    return count