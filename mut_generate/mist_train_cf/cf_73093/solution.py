"""
QUESTION:
Write a function `fibo_prime_product(n)` that calculates the product of the prime numbers in the Fibonacci series up to the nth term. The function should handle negative input by returning "Invalid input. The term must be a positive integer." and potential overflow scenarios by returning "Product of prime numbers in the Fibonacci series up to the nth term will cause overflow." The function should only consider prime numbers that are Fibonacci numbers in the sequence up to the nth term.
"""

def fibo_prime_product(n):
    if n <= 0:
        return "Invalid input. The term must be a positive integer."
    
    def is_prime(num):
        if num <= 1:
            return False
        elif num == 2 or num == 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        w = 2

        while i * i <= num:
            if num % i == 0:
                return False

            i += w
            w = 6 - w

        return True

    a, b = 0, 1
    prime_product = 1

    for _ in range(2, n + 1):
        a, b = b, a + b
        if is_prime(a):
            if prime_product > 0 and a > (9223372036854775807 // prime_product):
                return "Product of prime numbers in the Fibonacci series up to the nth term will cause overflow."
            else:
                prime_product *= a

    return prime_product