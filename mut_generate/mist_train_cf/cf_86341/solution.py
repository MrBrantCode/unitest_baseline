"""
QUESTION:
Implement a function called `is_prime` to check if a given number in a sorted array is prime, and use a while loop along with binary search to iterate over the array and print all the prime numbers. The function should return a boolean value indicating whether a number is prime or not, and the binary search should find all prime numbers in the array.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True