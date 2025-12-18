"""
QUESTION:
Write a function `smallest_prime_index` that returns the index of the last occurrence of the smallest prime number in an array of integers. The array may contain negative numbers and duplicates. If the array has a length of less than 3, return -1.
"""

def smallest_prime_index(array):
    if len(array) < 3:
        return -1
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    smallest_prime = float('inf')
    smallest_prime_index = -1
    
    for i in range(len(array)):
        if is_prime(array[i]) and array[i] <= smallest_prime:
            smallest_prime = array[i]
            smallest_prime_index = i
    
    return smallest_prime_index