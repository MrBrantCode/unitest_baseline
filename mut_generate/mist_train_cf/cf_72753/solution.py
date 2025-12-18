"""
QUESTION:
Write a recursive function called `primes_in_binary` that takes an integer `n` as input and prints a list of binary representations of all prime numbers from 2 to `n`, separated by semicolons. The function should not use a while-loop or any iterative approach, and it should not exceed Python's recursion limit.
"""

def prime_check(n, i=2): 
    # n is not prime if it is less than 2 or can be divided by i 
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    # check for the next divisor
    return prime_check(n, i + 1)

def convert_to_binary(n):
    return bin(n).replace("0b", "")

def primes_in_binary(n, i=2):
    if i <= n:
        if prime_check(i):
            print(convert_to_binary(i),end=';')
        primes_in_binary(n, i + 1)