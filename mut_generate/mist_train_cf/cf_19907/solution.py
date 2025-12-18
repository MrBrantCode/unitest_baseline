"""
QUESTION:
Write a function named `first_prime_divisible_by_five` that finds the first prime number in a list that is divisible by 5 and falls within the range of 11 to 99 (inclusive).
"""

def first_prime_divisible_by_five(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in numbers:
        if 11 <= num <= 99 and num % 5 == 0 and is_prime(num):
            return num