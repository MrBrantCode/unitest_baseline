"""
QUESTION:
Create a function named `average_of_primes` that takes a list as input and returns the average of all the prime numbers in the list, ignoring any non-integer values. If the list contains no prime numbers, return -1.
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