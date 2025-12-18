"""
QUESTION:
Generate the nth Fibonacci number using an iterative, memory-efficient method without relying on recursive calls, and classify whether the generated number is prime or not. Implement two functions: `fibonacci(n)` to calculate the nth Fibonacci number, and `is_prime(num)` to check if a given number is prime. Note that the solution should be able to handle large values of n, and the primality test should be efficient for large numbers.
"""

def fibonacci_and_prime(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    def is_prime(num):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    return a, is_prime(a)