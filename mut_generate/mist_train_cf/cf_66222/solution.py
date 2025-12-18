"""
QUESTION:
Create a function `classify_number(num)` that takes an integer `num` as input and returns a string indicating whether the number is 'prime', 'composite', or 'neither'. The function should correctly handle negative numbers, zero, and one as 'neither', and classify other numbers as 'prime' or 'composite' based on their divisibility properties. The function should be implemented using a helper lambda function `is_prime(num)` that checks if a number is prime.
"""

# Define a lambda function for checking if number is prime only
is_prime = lambda num: all(num%j != 0 for j in range(2, int(num**0.5)+1)) and num > 1

# Define a main function for classifying numbers
def classify_number(num):
    if num in (-1, 0, 1):
        return 'neither'
    elif is_prime(num):
        return 'prime'
    else:
        return 'composite'