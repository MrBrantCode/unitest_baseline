"""
QUESTION:
Create a function `is_prime` that takes an integer `num` as input and returns a boolean indicating whether `num` is prime. The function should optimize prime checking by only checking divisibility up to the square root of `num`. Additionally, create a `main` function that prompts the user for an integer `n` (greater than 1), generates a list of 'prime' and 'not prime' strings representing the primality of numbers from 0 to `n-1`, and prints this list. The `main` function should handle invalid inputs (non-integer or less than 2) by displaying an error message and prompting the user for a valid input.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True