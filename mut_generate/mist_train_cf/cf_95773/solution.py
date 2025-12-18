"""
QUESTION:
Write a function named `filter_primes` that takes an array of integers as input and returns a new array containing only the prime numbers greater than 2 from the input array. The function should have a time complexity of O(n) and should not use any built-in functions or libraries that directly check for prime numbers.
"""

def filter_primes(arr):
    def is_prime(n):
        # Check if n is prime
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Create a new array to store the filtered prime numbers
    filtered_arr = []
    for num in arr:
        if is_prime(num) and num > 2:
            filtered_arr.append(num)
    return filtered_arr