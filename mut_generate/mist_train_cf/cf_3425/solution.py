"""
QUESTION:
Create a function named `get_prime_elements` that takes an array of integers as input and returns a new array containing the elements at prime indices in the input array that are also prime numbers themselves. The output array should be sorted in descending order.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_elements(arr):
    primeElements = []
    for i in range(len(arr)):
        if is_prime(i) and is_prime(arr[i]):
            primeElements.append(arr[i])
    primeElements.sort(reverse=True)
    return primeElements