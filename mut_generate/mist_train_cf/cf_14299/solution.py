"""
QUESTION:
Create a function `is_prime()` and another function to combine two arrays `arr1` and `arr2`, and output an array containing unique elements that are prime numbers from both input arrays. Restrictions: The output array should only include unique prime numbers, and numbers in the output array should be in the order they first appear in the combined input arrays.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_combine(arr1, arr2):
    result = []
    for num in arr1 + arr2:
        if is_prime(num) and num not in result:
            result.append(num)
    return result