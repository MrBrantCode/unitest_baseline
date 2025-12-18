"""
QUESTION:
Create a program with two functions: `fibonacci(n)` and `isPrime(n)`. The `fibonacci(n)` function should recursively calculate the nth Fibonacci number. The `isPrime(n)` function should check if the given number is prime. Use these functions to compute and print the nth Fibonacci number and identify whether it is a prime number or not, without using any pre-defined libraries for Fibonacci or prime number calculation. The input `n` should be a positive integer.
"""

def fibonacci(n):
    if n<=0:
        return "Invalid input, n must be positive"
    elif n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else:
       return fibonacci(n-1) + fibonacci(n-2)

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True