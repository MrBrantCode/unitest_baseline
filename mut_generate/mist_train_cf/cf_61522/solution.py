"""
QUESTION:
Write a function `find_divisors_in_base` that takes two integers `n` and `base` as input, finds all the divisors of `n` and converts them to the specified `base`, then returns the list of divisors in the new base and their corresponding values in base 10. The function should use another function `convert_to_base` to convert numbers to the specified base and another function `convert_from_base` to convert numbers back to base 10. The `convert_from_base` function should be able to handle numbers with digits greater than 9 in the given base.
"""

def convert_to_base(n, base):
    alphabets = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < base:
        return alphabets[n]
    else:
        return convert_to_base(n // base, base) + alphabets[n % base]

def convert_from_base(n, base):
    return int(n, base)

def find_divisors_in_base(n, base):
    """
    Finds all the divisors of n, converts them to the specified base, 
    and returns the list of divisors in the new base and their corresponding values in base 10.

    Args:
    n (int): The number to find divisors for.
    base (int): The base to convert divisors to.

    Returns:
    list: A list of tuples containing divisors in the new base and their corresponding values in base 10.
    """
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    converted_divisors = [convert_to_base(d, base) for d in divisors]
    return list(zip(converted_divisors, [convert_from_base(d, base) for d in converted_divisors]))