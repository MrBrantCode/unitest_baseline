"""
QUESTION:
Create a recursive Python function named `fibonacci` that generates the Fibonacci series up to the nth term, and for each term, determine whether it's prime or not. Use a helper function `check_prime` to check if a number is prime. The function should take no arguments other than the term number `n`. Assume the first Fibonacci number is 0 (F0 = 0) and the second Fibonacci number is 1 (F1 = 1).
"""

def fibonacci(n):
    if n <= 1:
       return n
    else:
       return fibonacci(n-1) + fibonacci(n-2)

def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return "Not Prime"
        else:
            return "Prime"
    else:
        return "Not Prime"