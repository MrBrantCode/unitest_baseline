"""
QUESTION:
Create a function named `find_max_prime_subarray` that takes two parameters: an array of integers and an integer k, where k is the length of the subarray. The function should return the maximum sum of a subarray of length k that consists only of prime numbers. If there are less than k prime numbers in the array, return 0. The function should use a helper function named `is_prime` to check if a number is prime.
"""

def find_max_prime_subarray(array, k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in array if is_prime(num)]
    
    if len(primes) < k:
        return 0
    
    max_sum = sum(primes[:k])
    current_sum = max_sum
    
    for i in range(k, len(primes)):
        current_sum += primes[i] - primes[i-k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum