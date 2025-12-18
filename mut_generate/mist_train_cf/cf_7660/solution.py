"""
QUESTION:
Write a function named `get_prime_product` that takes a list of positive integers as input. The function should return a tuple containing the product of all unique prime numbers in the list greater than 10 and a list of these prime numbers in descending order.
"""

import math

def get_prime_product(numbers):
    prime_nums = []
    product = 1

    for num in numbers:
        if num > 10 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            if num not in prime_nums:
                prime_nums.append(num)
            if num not in prime_nums[:-1]:
                product *= num

    prime_nums.sort(reverse=True)
    return product, prime_nums