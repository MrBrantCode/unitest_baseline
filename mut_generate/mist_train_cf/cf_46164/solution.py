"""
QUESTION:
Create a function `mode` that calculates the mode of a list of integers without using any built-in Python functions. The function should handle lists with both prime and non-prime number of elements. If the length of the list is a prime number, return the mode of the prime counts; otherwise, return the mode of the non-prime counts. If the list is empty, return `None`.
"""


def is_prime(n: int):
    """Helper function to check if a number is prime."""
    if n < 2: return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mode(lst: list):
    if not lst: 
        return None 
    frequency = {} 
    for num in lst: 
        frequency[num] = frequency.get(num, 0) + 1 
      
    primes, non_primes = {}, {} 
    for num, freq in frequency.items(): 
        if is_prime(freq): 
            primes[num] = freq 
        else: 
            non_primes[num] = freq 
      
    if is_prime(len(lst)): 
        if primes: 
            return max(primes, key=primes.get) 
    else: 
        if non_primes: 
            return max(non_primes, key=non_primes.get) 
            
    return max(frequency, key=frequency.get)