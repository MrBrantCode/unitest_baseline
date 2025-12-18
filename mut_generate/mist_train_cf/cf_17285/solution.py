"""
QUESTION:
Create a function named `nth_prime_fibonacci(n)` that takes an integer `n` and returns the `n`-th prime Fibonacci number. The function should handle `n` up to 1000, have a time complexity of O(N^2) or better, and a space complexity of O(1) or O(log N).
"""

def nth_prime_fibonacci(n):
    if n <= 0:
        return None

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    count = 0
    a, b = 0, 1

    while count < n:
        if is_prime(b):
            count += 1
        a, b = b, a + b

    return a