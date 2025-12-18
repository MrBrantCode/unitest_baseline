"""
QUESTION:
Write a function `count_prime_numbers(arr)` that takes an array of integers as input and returns the count of prime numbers in the array. The array may contain both positive and negative integers. The function should use a for loop and an if statement to check for prime numbers.
"""

def count_prime_numbers(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for num in arr:
        if num > 1 and is_prime(num):
            count += 1
    return count