"""
QUESTION:
Write a function `smallest_prime_index` that returns the index of the smallest prime number in an array of integers. The array can contain negative numbers and duplicates. If there are multiple occurrences of the smallest prime number, return the index of the last occurrence. If the array length is less than 3, return -1.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def smallest_prime_index(array):
    if len(array) < 3:
        return -1
    
    smallest_prime = float('inf')
    smallest_prime_index = -1
    
    for i in range(len(array)):
        if is_prime(array[i]) and array[i] <= smallest_prime:
            smallest_prime = array[i]
            smallest_prime_index = i
    
    return smallest_prime_index