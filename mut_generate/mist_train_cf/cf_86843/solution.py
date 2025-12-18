"""
QUESTION:
Write a function `extract_prime_numbers` that takes a string `input_str` as input, extracts all prime numbers from the string, and returns them as a sorted list in descending order. The string can contain special characters, and the numbers in the string are positive integers. If no prime numbers are found, return an empty list.
"""

import re

def extract_prime_numbers(input_str):
    # Find all numbers in the input string
    numbers = re.findall(r'\d+', input_str)
    
    # Filter out non-prime numbers
    primes = []
    for num in numbers:
        num = int(num)
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    
    # Sort the prime numbers in descending order
    primes.sort(reverse=True)
    
    return primes