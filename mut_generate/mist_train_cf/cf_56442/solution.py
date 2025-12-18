"""
QUESTION:
Write a function `mode(l: list)` that takes a list of integers as input. The function should return the most frequent number in the list based on the following conditions:
- If the length of the list is a prime number, return the number with the highest frequency among the numbers that have a prime frequency.
- If the length of the list is not a prime number, return the number with the highest frequency among the numbers that have a non-prime frequency.
- If there are no numbers that meet the above conditions, return the most frequent number in the list. 

Note: You can use a helper function `is_prime(n: int)` to check if a number is prime.
"""

def is_prime(n: int):
    """Helper function to check if a number is prime."""
    if n < 2: 
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mode(l: list):
    if not l: 
        return None 
    frequency = {} 
    for num in l: 
        frequency[num] = frequency.get(num, 0) + 1 

    primes, non_primes = {}, {} 
    for num, freq in frequency.items(): 
        if is_prime(freq): 
            primes[num] = freq 
        else: 
            non_primes[num] = freq 

    if is_prime(len(l)): 
        if primes: 
            return max(primes, key=primes.get) 
    else:
        if non_primes: 
            return max(non_primes, key=non_primes.get) 

    return max(frequency, key=frequency.get)