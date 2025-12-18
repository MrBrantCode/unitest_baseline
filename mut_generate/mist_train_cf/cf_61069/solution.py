"""
QUESTION:
Create a function called `partition` that takes a list of integers as input and returns a list of two lists. The first inner list contains all the prime numbers from the input list, and the second inner list contains all the Fibonacci numbers from the input list. Exclude any integers that do not meet these criteria. Ensure the solution has a time complexity of O(n*sqrt(m)) and space complexity of O(n), where n is the number of elements in the input list and m is the maximum value in the input list.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    if n < 2:
        return True
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a+b
    return False

def partition(lst):
    primes = []
    fibos = []
    for i in lst:
        if is_prime(i):
            primes.append(i)
        elif is_fibonacci(i):
            fibos.append(i)
    return [primes, fibos]