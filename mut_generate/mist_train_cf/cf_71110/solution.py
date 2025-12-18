"""
QUESTION:
Write a function called `primeChecker` that takes a list of integers as input and returns two lists, one containing all prime numbers from the input list and the other containing all non-prime numbers. The function should be optimized for searching large datasets. The input list may contain duplicate numbers and may be empty. The function should not include the number 1 in the prime numbers list, as 1 is not considered a prime number.
"""

import math

def primeChecker(numbers):
    prime = []
    nonprime = []
    for num in numbers:
        if num > 1:
            for i in range(2, int(math.sqrt(num))+1):
                if (num % i) == 0:
                    nonprime.append(num)
                    break
            else:
                prime.append(num)
    return prime, nonprime