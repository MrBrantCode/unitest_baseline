"""
QUESTION:
Create a function called `validate_inputs` that takes a number and a string as parameters. The number should be in the range -1000 to 1000 (inclusive) and a prime number. The string should have a length of at least 10 characters and only contain alphabetical characters. If these conditions are met, return an array with the number and string; otherwise, return an empty array.
"""

def validate_inputs(num, string):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if num < -1000 or num > 1000:
        return []
    if len(string) < 10 or not string.isalpha():
        return []
    if not is_prime(num):
        return []
    return [num, string]