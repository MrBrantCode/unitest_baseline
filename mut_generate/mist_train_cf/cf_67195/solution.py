"""
QUESTION:
Create a function named `identify_primes` that takes a list of integers as input. The function should return a dictionary where each key is a number from the input list and the corresponding value is a boolean indicating whether the number is prime (True) or not (False). The function should handle the following edge cases: 

- Return 'Invalid' for negative integers and zero.
- Return 'Incorrect Input Type' if the input isn't a list or if any of the list elements aren't integers.
"""

def identify_primes(numbers):
    def is_prime(num):
        if num <= 0:
            return 'Invalid'
        if not isinstance(num, int):
            return 'Incorrect Input Type'
        if num == 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if not isinstance(numbers, list):
        return 'Incorrect Input Type'

    result = {}
    for num in numbers:
        result[num] = is_prime(num)
    
    return result