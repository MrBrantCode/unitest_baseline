"""
QUESTION:
Design a function `find_nth_prime_fibonacci(n)` that takes an integer `n` as input and returns the nth prime number in the Fibonacci sequence. The Fibonacci sequence starts with [0, 1] and each subsequent number is the sum of the previous two. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nth_prime_fibonacci(n):
    count = 0
    fib_seq = [0, 1]
    
    while count < n:
        if is_prime(fib_seq[-1]):
            count += 1
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    return fib_seq[-2]