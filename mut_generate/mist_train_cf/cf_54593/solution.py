"""
QUESTION:
Construct an algorithm that can locate the nth prime number in a given array of arbitrary length and structure. The function should be named `find_nth_prime` and should take two parameters: an array of integers and an integer `n`. The function should return the nth prime number in the array. The solution should not use library functions. If the nth prime number does not exist in the array, the function should return `None`.
"""

def is_prime(num):
    # Avoid error cases
    if num < 2:
        return False
    elif num == 2:
        return True
    # Check for divisibility on numbers less than num
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find_nth_prime(arr, n):
    prime_count = 0
    for value in arr:
        if is_prime(value):
            prime_count += 1
            if prime_count == n:
                return value
    return None