"""
QUESTION:
Write a function `sum_prime_digits_average(a, b, c)` that calculates the sum of prime digits of three positive integers `a`, `b`, and `c`, then returns their average. Prime digits are 2, 3, 5, and 7. If a number has no prime digits, it does not contribute to the average. If all numbers have no prime digits, return 0.
"""

def sum_prime_digits_average(a, b, c):
    sum_prime_digits = 0
    count = 0

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_digits(n):
        return sum(int(digit) for digit in str(n))

    for number in [a, b, c]:
        prime_digits_sum = 0
        for digit in str(number):
            digit = int(digit)
            if digit in [2, 3, 5, 7]:
                prime_digits_sum += digit
        if prime_digits_sum > 0:
            count += 1
            sum_prime_digits += prime_digits_sum

    if count == 0:
        return 0
    return sum_prime_digits / count