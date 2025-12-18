"""
QUESTION:
Write a function `largest_prime` that finds the largest prime number in an array of integers and returns this prime number along with its index. The function should handle duplicate values, cases with multiple largest prime numbers, and cases where the array is empty or contains only non-prime numbers. If there are multiple largest prime numbers, return the index of the first occurrence. If the array is empty or contains only non-prime numbers, return -1 as the index and 0 as the largest prime number.
"""

def largest_prime(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = 0
    max_prime_index = -1

    for i, num in enumerate(arr):
        if is_prime(num):
            if num > max_prime:
                max_prime = num
                max_prime_index = i
    return max_prime, max_prime_index