"""
QUESTION:
Create a function `process_list_of_tuples` that takes a list of tuples, where each tuple contains a key-value pair. The function should process the list and return a dictionary where each key is associated with a list of values. 

The function should follow these rules:
- If a key already exists in the dictionary, append the value to the existing list of values for that key.
- If a key does not exist in the dictionary, create a new key-value pair.
- If a value is a prime number, remove the key-value pair from the dictionary.
- If a value is not a prime number, calculate the factorial of the value and check if it is a prime number. If the factorial is not a prime number, add the key-value pair to the dictionary.
- If the factorial of a value is a prime number, skip the current tuple.

Note: The function should return the processed dictionary.
"""

import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def process_list_of_tuples(list_of_tuples):
    """Process a list of tuples into a dictionary."""
    result = {}
    
    for key, value in list_of_tuples:
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
            
        if is_prime(value):
            if key in result:
                del result[key]
        else:
            factorial = math.factorial(value)
            if not is_prime(factorial):
                if key in result and value not in result[key]:
                    result[key].append(value)
    return result