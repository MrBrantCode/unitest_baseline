"""
QUESTION:
Create a function called `is_prime` that takes two positive integers as input, `num1` and `num2`. The function should return a list of prime numbers between `num1` and `num2` (inclusive) that are not divisible by both 2 and 3. If either `num1` or `num2` is not a positive integer, the function should return an error message.
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