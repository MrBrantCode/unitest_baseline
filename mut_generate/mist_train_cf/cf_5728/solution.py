"""
QUESTION:
Write a function named `sum_even_numbers` that takes a list of integers as input and returns the sum of all even numbers in the list that meet the following conditions: 
- the number is not divisible by 3 or 5 
- the number is not a prime number 
- the number has a prime number of digits 
- the number is considered in descending order of the original list.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def has_prime_number_of_digits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return is_prime(count)

def sum_even_numbers(lst):
    lst.sort(reverse=True)
    result = 0
    for num in lst:
        if num % 2 == 0 and not is_prime(num) and not num % 3 == 0 and not num % 5 == 0 and has_prime_number_of_digits(num):
            result += num
    return result