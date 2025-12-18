"""
QUESTION:
Create a 5x5 2D array where each element is a unique prime number greater than 100.
"""

def generate_primes_array(rows: int, cols: int, start: int) -> list:
    """
    Generate a 2D array filled with unique prime numbers.

    Args:
    rows (int): Number of rows in the array.
    cols (int): Number of columns in the array.
    start (int): Starting number for prime number generation.

    Returns:
    list: A 2D array filled with unique prime numbers.
    """
    def is_prime(n: int) -> bool:
        """
        Check if a number is prime.

        Args:
        n (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = []
    num = start
    while len(primes) < rows * cols:
        if is_prime(num):
            primes.append(num)
        num += 1

    return [primes[i:i + cols] for i in range(0, len(primes), cols)]

# Generate a 5x5 2D array with unique prime numbers greater than 100
primes_array = generate_primes_array(5, 5, 100)