"""
QUESTION:
Write a function called `nth_prime_increment` that takes an integer `x` as input, increments it by the nth prime number, where n is the sum of the digits of `x` squared, and returns the updated value.
"""

def nth_prime_increment(x):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    digit_sum = sum(int(digit) for digit in str(x)) ** 2

    count = 0
    n = 2
    while count < digit_sum:
        if is_prime(n):
            count += 1
        n += 1
    nth_prime = n - 1

    return x + nth_prime