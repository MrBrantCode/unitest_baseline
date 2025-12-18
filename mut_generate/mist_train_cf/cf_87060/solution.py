"""
QUESTION:
Implement a function `fibonacci(n)` that prints the first `n` Fibonacci numbers and also prints the sum of the prime numbers in the series. The function should have a time complexity of O(n) and a space complexity of O(1), and should not use any additional data structures that scale with input size `n`. The input `n` is a non-negative integer.
"""

def fibonacci(n):
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b = 0, 1
    sum_primes = 0
    for _ in range(n):
        print(a)
        if is_prime(a):
            sum_primes += a
        a, b = b, a + b
    print("Sum of prime numbers:", sum_primes)