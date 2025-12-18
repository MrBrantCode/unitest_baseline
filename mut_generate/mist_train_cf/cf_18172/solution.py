"""
QUESTION:
Write a function `sum_of_primes` that takes a list of integers as input and returns a tuple containing the sum and count of prime numbers in the list that are greater than 100 and less than 1000. If no prime numbers meet this criteria, return 0.
"""

def entrance(lst):
    primes = []
    for num in lst:
        if num > 100 and num < 1000:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    
    if len(primes) == 0:
        return 0
    else:
        return sum(primes), len(primes)