"""
QUESTION:
Given an array of positive integers and a target sum value, find the three smallest prime numbers in the array whose sum equals the target value and whose product is also a prime number.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def entrance(array, value):
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
    
    return primes[:3]  # Return the three smallest primes