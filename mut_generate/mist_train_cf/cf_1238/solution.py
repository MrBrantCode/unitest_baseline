"""
QUESTION:
Create a function `extract_prime_numbers` that takes a string as input, extracts all prime numbers from it that are in a string containing at least one special character, and returns them as a list in descending order. The input string can be of any length and may contain multiple occurrences of special characters. Special characters are considered as any non-alphanumeric characters. If no prime numbers are found, return an empty list.
"""

import re

def extract_prime_numbers(input_str):
    # Find all substrings containing at least one special character
    substrings = re.findall(r'.*[^\w\s].*', input_str)
    
    # Find all numbers in the substrings
    numbers = re.findall(r'\d+', ''.join(substrings))
    
    # Filter out non-prime numbers
    primes = set()
    for num in numbers:
        num = int(num)
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.add(num)
    
    # Return the prime numbers in descending order
    return sorted(primes, reverse=True)