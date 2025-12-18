"""
QUESTION:
Create a function called `validate_inputs` that takes two parameters: an integer `num` and a string `string`. The `num` parameter must be in the range of -1000 to 1000 (inclusive) and be a prime number. The `string` parameter must be at least 10 characters long and only contain alphabetical characters. If either condition is not met, the function should return an empty list. Otherwise, it should return a list containing `num` and `string`.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def validate_inputs(num, string):
    if num < -1000 or num > 1000:
        return []
    if len(string) < 10 or not string.isalpha():
        return []
    if not is_prime(num):
        return []
    return [num, string]