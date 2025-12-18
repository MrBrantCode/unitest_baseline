"""
QUESTION:
Create a function `check_prime` that takes three arguments: a positive integer `num` between 1 and 1000 (inclusive), a boolean `boolean` that is true, and a list of strings `prime_list` containing unique prime numbers between 2 and 1000 (inclusive) represented as strings. The function should return "yes" if the `boolean` is true and `num` is a prime number that is present in `prime_list`, else it should return "no".
"""

def check_prime(num, boolean, prime_list):
    if boolean and num > 0 and num <= 1000:
        num_str = str(num)
        if num_str in prime_list:
            return "yes"
    return "no"