"""
QUESTION:
Find the three smallest prime numbers in an array of positive integers that sum up to a given value and whose product is also a prime number. Implement a function `find_smallest_primes(array, value)` that takes an array of positive integers and a target sum as input, and returns a list of tuples, where each tuple contains three prime numbers from the array that meet the specified conditions.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_smallest_primes(array, value):
    primes = []
    
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                a, b, c = array[i], array[j], array[k]
                
                if a + b + c == value:
                    product = a * b * c
                    if is_prime(product):
                        primes.append((a, b, c))
    
    primes.sort(key=sum)
    
    return primes[:3]