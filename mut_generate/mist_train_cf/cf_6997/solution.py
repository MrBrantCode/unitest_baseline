"""
QUESTION:
Write a function `sum_even_greater_than_10` that takes a dictionary as input. The function should return the sum of all integer values in the dictionary that are even numbers greater than 10, excluding prime numbers. If a value in the dictionary is a string representation of a number, it should be converted to an integer before checking. If no even numbers greater than 10 exist in the dictionary, the function should return -1.
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