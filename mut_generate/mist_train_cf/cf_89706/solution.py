"""
QUESTION:
Implement a function `sum_even_greater_than_10` that takes a dictionary as input and returns the sum of its even integer values greater than 10, excluding prime numbers. If a value is a string representation of a number, it should be converted to an integer before being considered. If no such values exist in the dictionary, return -1.
"""

def sum_even_greater_than_10(dictionary):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    total = 0
    has_even_greater_than_10 = False
    for value in dictionary.values():
        if isinstance(value, str):
            value = int(value)
        if isinstance(value, int) and value > 10 and value % 2 == 0 and not is_prime(value):
            total += value
            has_even_greater_than_10 = True

    if has_even_greater_than_10:
        return total
    else:
        return -1