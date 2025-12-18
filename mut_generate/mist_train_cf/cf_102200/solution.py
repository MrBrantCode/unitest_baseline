"""
QUESTION:
Write a function called `is_prime(num)` that checks if a given number `num` is prime or not and returns a boolean value. Use this function to evaluate the condition `cond` where `cond` must be greater than 10, divisible by 2, 3, 5, and 7, and a prime number. If `cond` satisfies all conditions, print "true", otherwise print "false". The input `cond` can be any integer.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True