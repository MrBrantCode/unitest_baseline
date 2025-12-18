"""
QUESTION:
Create a function called `fibonacci_primes(n)` that generates the Fibonacci sequence up to the nth term and returns a list of unique prime numbers from the sequence in ascending order. The function should only accept integers between 1 and 10,000 (inclusive) and return an error message for invalid inputs.
"""

def fibonacci_primes(n):
    if not isinstance(n, int) or n < 1 or n > 10**4:
        return "Invalid input! Please enter an integer between 1 and 10000."

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    
    prime_fibs = [num for num in fibs if is_prime(num)]

    return sorted(list(set(prime_fibs)))