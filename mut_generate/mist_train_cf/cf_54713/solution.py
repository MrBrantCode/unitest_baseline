"""
QUESTION:
Create a function named `advanced_calc` that takes a non-empty list of integers `lst` and an integer `n` as parameters. The function should return the product of the elements in the list that are Fibonacci numbers, are at prime indices, and are divisible by `n`.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    """Check if a number is a Fibonacci number."""
    if n == 0 or n == 1:
        return True
    fibs = [0, 1]
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])
    return n == fibs[-1]

def advanced_calc(lst, n):
    product = 1
    for i in range(len(lst)):
        if lst[i] % n == 0 and is_prime(i) and is_fibonacci(lst[i]):
            product *= lst[i]
    return product