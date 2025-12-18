"""
QUESTION:
Write two functions, `cumulative_total(n)` and `cumulative_primes_total(n)`, to calculate the cumulative total of all positive integers and prime numbers from 0 to a specified number 'n', respectively. The function `cumulative_total(n)` should have a time complexity of O(1) and `cumulative_primes_total(n)` should be optimized for large input sizes, but does not necessarily have to be the most efficient solution. The input 'n' is a non-negative integer.
"""

def cumulative_total(n):
    return n*(n+1)//2

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while (i * i <= num):
        if (num%i == 0 or num%(i + 2) == 0):
            return False
        i += 6
    return True

def cumulative_primes_total(n):
    total = 0
    for num in range(2, n + 1):
        if is_prime(num):
            total += num
    return total