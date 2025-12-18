"""
QUESTION:
Write a function `seven_six_ten(n)` that returns the count of prime numbers not exceeding `n`, containing the digit 7, and having a digit sum divisible by 2.
"""

def seven_six_ten(n: int) -> int:
    def is_prime(num):
        if num in (2, 3):
            return True
        if num < 2 or num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def has_seven(num):
        return '7' in str(num)

    def digit_sum_divisible_by_2(num):
        return sum(int(digit) for digit in str(num)) % 2 == 0

    counter = 0

    for i in range(2, n + 1):
        if (
            is_prime(i) and
            has_seven(i) and
            digit_sum_divisible_by_2(i)
        ):
            counter += 1

    return counter