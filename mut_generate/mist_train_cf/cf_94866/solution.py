"""
QUESTION:
Create a function `sort_binary_primes(lst)` that takes a list of integers as input and returns a list of prime numbers in descending order. Each number in the input list should be converted to its binary representation with a minimum length of 6 digits. The function should filter out non-prime numbers and return the sorted list of prime numbers. The input list can contain any integers. The output list should be sorted in descending order.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sort_binary_primes(lst):
    binary_list = []
    for num in lst:
        binary = bin(num)[2:].zfill(6)
        binary_list.append(binary)
    
    prime_list = []
    for bin_num in binary_list:
        decimal_num = int(bin_num, 2)
        if is_prime(decimal_num):
            prime_list.append(decimal_num)
    
    prime_list = sorted(prime_list, reverse=True)
    return prime_list