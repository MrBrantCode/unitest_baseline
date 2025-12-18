"""
QUESTION:
Create a function called `generate_prime_fibonacci` that takes an integer `n` as input and returns a list of the first `n` Fibonacci numbers that are prime and in ascending order. The function should only include prime numbers in the sequence and each number must be greater than the previous one. Note that generating long sequences can be computationally intensive.
"""

def generate_prime_fibonacci(n):
    """
    Generate the first n Fibonacci numbers that are prime and in ascending order.

    Args:
    n (int): The number of prime Fibonacci numbers to generate.

    Returns:
    list: A list of the first n prime Fibonacci numbers in ascending order.
    """
    
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci():
        """Generate Fibonacci numbers."""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    prime_fibonacci = []
    fib = fibonacci()
    while len(prime_fibonacci) < n:
        num = next(fib)
        if is_prime(num):
            prime_fibonacci.append(num)
    return prime_fibonacci