"""
QUESTION:
Create two functions, `check_prime(n)` and `fibonacci(n)`, to generate the Fibonacci sequence up to the nth term and check if each number in the sequence is prime. The `check_prime(n)` function should return `True` if `n` is prime and `False` otherwise. The `fibonacci(n)` function should return a list of integers representing the Fibonacci sequence up to the nth term. The functions should not take any additional arguments besides `n`, which is a positive integer.
"""

def is_prime(n):
    """Check if a number is prime."""
    # number of integers less than n to check for factors
    prime_check = range(2, n)

    # for each possible factor
    for i in prime_check:
        # if a factor is found, n is not prime
        if n % i == 0:
            return False
        # if no factor was found, n is prime
    return True


def fibonacci(n):
    """Generate Fibonacci sequence up to the nth term."""
    fib_seq = []
    a, b = 0, 1
    
    while n:
        fib_seq.append(a)
        a, b = b, a + b
        n -= 1
    
    return fib_seq