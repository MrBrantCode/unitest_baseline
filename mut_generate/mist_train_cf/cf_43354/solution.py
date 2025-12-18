"""
QUESTION:
Write a function called `primes_and_fibos_product` that takes an array of numbers as input and returns the product of the first ten prime numbers and the first ten Fibonacci numbers found in the array. The function should handle arrays containing negative numbers, floating point numbers, and complex numbers, and should return an error message if there are less than ten prime or Fibonacci numbers in the array. The function should be optimized for performance and should be able to process large arrays efficiently.
"""

import math

def primes_and_fibos_product(arr):
    def is_prime(n):
        if n == 1 or n <= 0 or n % 1 > 0:
            return False
        sqrt_n = int(math.sqrt(n))
        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                return False
        return True

    def is_fibonacci(n):
        if n < 0 or n % 1 > 0:
            return False
        x = 5 * n**2
        return math.isqrt(x + 4)**2 == (x + 4) or math.isqrt(x - 4)**2 == (x - 4)

    primes = []
    fibos = []
    result = 1
    
    for num in arr:
        if not isinstance(num, (int,float)) or isinstance(num, complex): 
            continue
        if is_prime(num) and len(primes) < 10:
            primes.append(num)
            result *= num
        if is_fibonacci(num) and len(fibos) < 10:
            fibos.append(num)
            result *= num

    if len(primes) < 10 or len(fibos) < 10:
        return "Error: Not enough prime or Fibonacci numbers in array"
    return result