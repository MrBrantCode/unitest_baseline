"""
QUESTION:
Write a function `extract_prime_integer(number: float) -> int` that takes a positive real number, extracts its integral part, and returns it if it is a prime number. If the integral part is not a prime number, the function should return None.
"""

def is_prime_number(n: int) -> bool:
    """Checks if a number is prime."""
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def extract_prime_integer(number: float) -> int:
    """Extracts the integral part of a number and returns it if it's prime."""
    int_part = int(number)
    return int_part if is_prime_number(int_part) else None