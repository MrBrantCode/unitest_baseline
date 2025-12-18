"""
QUESTION:
Create a function `is_prime` that takes one argument and `min_prime_num` that takes one argument, which is a list of integers. The `is_prime` function checks whether a number is prime or not and returns a boolean. The `min_prime_num` function returns the smallest prime number from the list. If there is no prime number in the list, the function should return `None`. The prime check should be efficient for large numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def min_prime_num(nums):
    min_prime = None
    for num in nums:
        if is_prime(num):
            if min_prime is None or num < min_prime:
                min_prime = num
    return min_prime