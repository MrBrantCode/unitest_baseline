"""
QUESTION:
Create a function named `check_prime` that takes three arguments: a positive integer `num` between 1 and 1000 (inclusive), a boolean `boolean` that is always true, and a list of prime numbers `prime_list` where each prime number is a positive integer between 2 and 1000 (inclusive). The function should return "yes" if `boolean` is true and `num` is present in `prime_list`, otherwise return "no".
"""

def check_prime(num, boolean, prime_list):
    if boolean and num in prime_list:
        return "yes"
    else:
        return "no"