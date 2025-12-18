"""
QUESTION:
Create a function `fibo_primes(p)` that generates Fibonacci numbers up to the specified number `p` and returns the prime numbers within the sequence. The function should use a helper function `is_prime(n)` to check if a number is prime. The input `p` is a positive integer and the output should be a list of prime numbers in the Fibonacci sequence.
"""

def is_prime(n):
    """Check if a number is a prime number"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fibo_primes(p):
    """Generate Fibonacci sequence and return prime numbers"""
    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] <= p:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    return [f for f in fib_seq if is_prime(f)]