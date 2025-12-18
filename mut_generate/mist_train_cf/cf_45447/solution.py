"""
QUESTION:
Given an array of prime numbers, write a function `find_next_prime` that takes the array as input and returns the next prime number after the last element in the array. The function should not use the Sieve of Eratosthenes algorithm to generate prime numbers up to a certain limit, but instead, should check each subsequent number to see if it is prime.
"""

import math

def find_next_prime(array):
    num = array[-1] + 1
    while True:
        isPrime = True
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
               isPrime = False
               break
        if isPrime:
            return num
        num += 1