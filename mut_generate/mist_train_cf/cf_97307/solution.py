"""
QUESTION:
Write a function `print_primes(n)` that prints all prime numbers between 1 and n without using a loop. The function should have a time complexity of O(log n) and a space complexity of O(1).
"""

def print_primes(n):
    if n < 2:  # base case: smallest prime number is 2
        return
    else:
        print_primes(n - 1)  # recursively call the function with n-1

    # check if n is prime
    if is_prime(n):
        print(n)  # print the prime number

def is_prime(num):
    if num < 2:  # 0 and 1 are not prime
        return False
    if num == 2:  # 2 is prime
        return True
    if num % 2 == 0:  # any even number is not prime
        return False

    # check odd divisors from 3 to sqrt(num)
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2  # increment by 2 to skip even divisors

    return True