"""
QUESTION:
Write a function `check_primes(lst)` that takes a list of integers as input and returns `True` if all numbers in the list are prime numbers, and `False` otherwise. The list can contain both positive and negative integers. The length of the list is at most 10^6 and the input numbers can be as large as 10^12. The time complexity of the solution should be O(n * sqrt(m)), where n is the length of the list and m is the maximum number in the list, and the space complexity should be minimized.
"""

def check_primes(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    for num in lst:
        if not is_prime(abs(num)):
            return False
    return True