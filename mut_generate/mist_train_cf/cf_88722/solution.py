"""
QUESTION:
Write a function `filter_primes` that takes an array of integers as input, filters out the elements that are prime numbers greater than 2, and returns them in a new array. The function should have a time complexity of O(n) and a space complexity of O(n), without using built-in functions or libraries for checking prime numbers.
"""

def filter_primes(arr):
    result = []
    for num in arr:
        if num <= 1:
            continue
        if num == 2:
            continue
        if num % 2 == 0:
            continue
        i = 3
        is_prime = True
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 2
        if is_prime and num > 2:
            result.append(num)
    return result