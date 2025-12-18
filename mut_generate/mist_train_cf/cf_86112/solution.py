"""
QUESTION:
Write a function called `multiply_primes` that takes a list of integers as input and returns the product of all prime digits (2, 3, 5, 7) found in the digits of these integers.
"""

def multiply_primes(num_list):
    pri_nums = [2, 3, 5, 7]  # prime numerals 0-9
    result = 1
    for num in num_list:
        for digit in str(num):
            if int(digit) in pri_nums:
                result *= int(digit)
    return result