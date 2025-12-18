"""
QUESTION:
Implement a function `sum_prime_fibonacci(numbers)` that calculates the sum of all prime numbers and Fibonacci numbers in the given array `numbers`, excluding negative numbers. The time complexity should be less than O(n^2) and the space complexity should be O(1), without using any additional data structures.
"""

def sum_prime_fibonacci(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_fibonacci(n):
        a, b = 0, 1
        while a <= n:
            if a == n:
                return True
            a, b = b, a + b
        return False

    result = 0
    for num in numbers:
        if num > 0 and (is_prime(num) or is_fibonacci(num)):
            result += num
    return result