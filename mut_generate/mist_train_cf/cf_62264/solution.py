"""
QUESTION:
Write a function named `missing_prime` that takes a list of prime numbers as input and returns a list of prime numbers that are missing from the input list, where the complete list of prime numbers is defined as all prime numbers between 2 and 100. The input list may not contain all prime numbers between 2 and 100, but it will only contain prime numbers between 2 and 100.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def missing_prime(arr):
    complete_list = [i for i in range(2, 101) if is_prime(i)]
    return [i for i in complete_list if i not in arr]