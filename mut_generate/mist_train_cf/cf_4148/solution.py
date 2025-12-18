"""
QUESTION:
Create a function sumPrimeEvenToN that takes an integer argument n and returns the sum of prime even numbers from 2 to n. A prime even number is an even number divisible only by 1 and itself. Note that n must be a positive integer.
"""

import math

def sumPrimeEvenToN(n):
    prime_even_numbers = []
    for num in range(2, n+1, 2):
        flag = True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                flag = False
                break
        if flag:
            prime_even_numbers.append(num)
    return sum(prime_even_numbers)