"""
QUESTION:
Write a function `calc_aggregate(num)` that calculates the sum of all prime numbers and the sum of all Fibonacci prime numbers less than a given number `num`. The function should return a tuple of two sums. The input number `num` will not exceed 1000.
"""

def calc_aggregate(num):
    # Function to check if number is prime
    def is_prime(n):
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

    # Function to check if number is Fibonacci
    def is_fibonacci(n): 
        x = 0
        y = 1
        while y < n: 
            z = x + y 
            x = y 
            y = z 
        return y == n

    # List to hold prime and Fibonacci prime numbers
    primes = []
    fib_primes = []

    # Check each number up to specified number
    for i in range(2, num):
        if is_prime(i):
            primes.append(i)
            if is_fibonacci(i):
                fib_primes.append(i)

    # Calculate sum of prime numbers and Fibonacci primes
    prime_sum = sum(primes)
    fib_prime_sum = sum(fib_primes)

    return prime_sum, fib_prime_sum