"""
QUESTION:
Write a function `sort_binary_primes(lst)` that takes a list of integers as input. Convert each integer in the list to its binary representation, ensuring a minimum length of 6 digits, and sort the resulting list in descending order. Only include integers in the output list if their corresponding binary representation corresponds to a prime number in decimal form.
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