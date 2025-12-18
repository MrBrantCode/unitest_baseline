"""
QUESTION:
Implement a function `fib_prime(n)` that generates the Fibonacci series up to the nth number and returns a list of prime numbers within the series. The function should ensure optimal time and space complexity, where n is a non-negative integer.
"""

def fib_prime(n):
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        sqrt_num = int(num**0.5) + 1
        for i in range(3, sqrt_num, 2):
            if num % i == 0:
                return False
        return True


    def fib(num, computed = {0: 0, 1: 1}):
        """Compute the nth Fibonacci number recursively with memoization."""
        if num not in computed:
            computed[num] = fib(num-1, computed) + fib(num-2, computed)
        return computed[num]


    """Generate the Fibonacci series till n and return the prime numbers within the series."""
    fib_nums = [fib(i) for i in range(n+1)]
    return [num for num in fib_nums if is_prime(num)]