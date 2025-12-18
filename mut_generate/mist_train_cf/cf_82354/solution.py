"""
QUESTION:
Write a function `cube_prime_numbers(n)` that prints the cube of prime numbers from 2 to `n` (inclusive) using a while loop. Ensure the function catches and handles any exceptions that may occur during execution.
"""

def cube_prime_numbers(n):
    """
    Print cube of prime numbers in range of (1, n)
    """
    def is_prime(num):
        """
        Check if number is prime
        """
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    i = 2
    while i <= n:
        try:
            if is_prime(i):
                print(i**3)
            i += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            break