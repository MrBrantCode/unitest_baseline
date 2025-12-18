"""
QUESTION:
Write a function named `check_prime_in_range` that takes an integer as input. The function should check whether the number is a prime number and is within a range of 10,000 to 20,000. Additionally, the number must be divisible by both 3 and 5.
"""

def check_prime_in_range(n):
    if 10000 <= n <= 20000 and all(n % i != 0 for i in range(2, int(n**0.5)+1)) and n % 3 == 0 and n % 5 == 0:
        return True
    else:
        return False