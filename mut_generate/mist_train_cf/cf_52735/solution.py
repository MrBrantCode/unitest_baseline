"""
QUESTION:
Create a function named `prime_fibonacci` that takes two parameters: `start` and `end`, both defaulting to 1 and 100 respectively. This function should generate all Fibonacci numbers within the given range, filter out non-prime numbers, and print the prime Fibonacci numbers. Implement error handling to ensure that `start` is less than `end` and both are positive integers. If the provided range is invalid, print "Invalid range" and return without generating any numbers.
"""

def prime_fibonacci(start = 1, end = 100):
    if end < start or start < 0 or end < 0:
        print("Invalid range")
        return
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if a > end:
            break
        if a >= start and is_prime(a):
            print(a)

def is_prime(n):
    if n < 2:
        return False
    for number in range(2, int(n ** 0.5) + 1):
        if n % number == 0:
            return False
    return True