"""
QUESTION:
Write a function named `sum_prime_fibonacci` that calculates the sum of all the prime numbers and Fibonacci numbers in a given array of numbers, excluding any negative numbers. The function should have a time complexity of less than O(n^2) and a space complexity of O(1), where n is the length of the input array. The function should return the calculated sum.
"""

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

def sum_prime_fibonacci(numbers):
    result = 0
    for num in numbers:
        if num > 0 and (is_prime(num) or is_fibonacci(num)):
            result += num
    return result