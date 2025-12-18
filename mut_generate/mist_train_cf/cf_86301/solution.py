"""
QUESTION:
Create a function `average_of_primes(lst)` that takes a list of integers as input and returns the average of all prime numbers in the list, ignoring non-integer values. If no prime numbers exist in the list, return -1.
"""

def average_of_primes(lst):
    primes = []
    for num in lst:
        if type(num) == int:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    primes.append(num)
    if len(primes) == 0:
        return -1
    else:
        return sum(primes) / len(primes)