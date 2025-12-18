"""
QUESTION:
Write a function `count_primes` that takes a list of integers as input and returns the number of prime numbers between -100 and 100 in the list. The function should use a for loop and an if statement. Note that prime numbers are defined as numbers greater than 1 that are divisible only by 1 and themselves.
"""

def count_primes(arr):
    count = 0
    for num in arr:
        if num > 1 and num <= 100:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                count += 1
    return count