"""
QUESTION:
Write a function `is_prime(n)` to check if a number `n` is prime. Then use this function to find the sum of all prime numbers from 1 to 1000, excluding 2 and 3. The function `is_prime(n)` should return a boolean value indicating whether `n` is prime or not. The sum should be calculated by iterating over the range from 1 to 1000, checking each number to see if it's prime (excluding 2 and 3), and adding it to the sum if it is.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True