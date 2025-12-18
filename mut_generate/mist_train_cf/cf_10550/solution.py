"""
QUESTION:
Create a function called `get_next_prime_fibonacci(n)` that takes an integer `n` as input and returns the next prime Fibonacci number after `n`. A prime number is a positive integer that is divisible only by itself and 1, and a Fibonacci number is a number in the sequence where each number is the sum of the two preceding ones (0, 1, 1, 2, 3, 5, 8, ...). The function should not take any other input and should return the next prime Fibonacci number, which is greater than `n`.
"""

def get_next_prime_fibonacci(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_fibonacci(num):
        a, b = 0, 1
        while b < num:
            a, b = b, a + b
        return b == num

    num = n + 1
    while True:
        if is_fibonacci(num) and is_prime(num):
            return num
        num += 1