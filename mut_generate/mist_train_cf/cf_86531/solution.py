"""
QUESTION:
Write a function that takes a range of positive integers as input and returns a list of numbers that are both prime and Fibonacci numbers within that range.

The function should take two parameters, start and end, representing the start and end of the range, inclusive.

The function should not use any built-in functions to check for primality or Fibonacci numbers, but instead implement these checks manually. 

For example, if the input range is 1 to 1000, the function should return all prime numbers within this range that are also Fibonacci numbers.
"""

def entrance(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_fibonacci(n):
        if n < 0:
            return False
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b == n

    result = []
    for num in range(start, end + 1):
        if is_prime(num) and is_fibonacci(num):
            result.append(num)
    return result