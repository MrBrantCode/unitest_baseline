"""
QUESTION:
Create a function `prime_fibonacci` that takes an array of integers as input. The function should return an array containing only the prime numbers from the input array that are also part of the Fibonacci sequence. The function should include error handling for non-integer inputs.
"""

def prime_fibonacci(numbers):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def is_fibonacci(n):
        x = 0
        y = 1
        while y < n:
            z = x + y
            x = y
            y = z
        return y == n

    try: 
        return [n for n in numbers if isinstance(n, int) and is_prime(n) and is_fibonacci(n)]
    except TypeError:
        return "Error: Non-integer input detected"