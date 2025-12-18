"""
QUESTION:
Write a function `is_prime(num1, num2)` that takes two positive integers as input and returns a list of prime numbers between `num1` and `num2` (inclusive) that are not divisible by both 2 and 3. The function should validate that the inputs are positive integers greater than zero and return an error message if the validation fails.
"""

def is_prime(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int) and num1 > 0 and num2 > 0:
        primes = []
        for num in range(num1, num2 + 1):
            if num > 1 and num % 2 != 0 and num % 3 != 0:
                primes.append(num)
        return primes
    else:
        return "Invalid input. Both numbers must be positive integers greater than zero."