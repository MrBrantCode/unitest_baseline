"""
QUESTION:
Create a function called `check_prime` that takes three arguments: a positive integer `num` between 1 and 1000 (inclusive), a boolean value `boolean` that is `True`, and a list of unique prime numbers `prime_list` represented as strings between 2 and 1000 (inclusive). The function should return "yes" if `boolean` is `True` and `num` is present in `prime_list`, otherwise return "no".
"""

def check_prime(num, boolean, prime_list):
    if boolean and num > 0 and num <= 1000:
        num_str = str(num)
        if num_str in prime_list:
            return "yes"
    return "no"