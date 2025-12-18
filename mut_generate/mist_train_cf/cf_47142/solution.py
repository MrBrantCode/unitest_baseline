"""
QUESTION:
Design a function `find_prime_numbers` that takes a list of numbers as input, identifies prime numbers, and returns a tuple containing a sorted list of prime numbers in ascending order and the product of all prime numbers. The function should handle exceptions for non-numerical inputs and floating-point numbers. The product should be calculated even if it exceeds the maximum limit for integers in Python.
"""

from functools import reduce
from operator import mul
import decimal

def find_prime_numbers(input_list):
    prime_numbers = []
    for num in input_list:
        try:
            num = int(num)
            if num < 2:
                continue
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
        except ValueError:
            pass
        except TypeError:
            pass

    prime_numbers.sort()
    prime_product = reduce(mul, map(decimal.Decimal, prime_numbers), 1)
    return prime_numbers, prime_product