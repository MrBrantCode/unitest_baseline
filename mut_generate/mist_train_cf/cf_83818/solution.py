"""
QUESTION:
Write a function `authenticate_and_filter` that takes a list of numbers as input, checks if all elements in the list are integers, and returns a list of prime numbers. If a non-integer value is detected, print a warning message.
"""

# Function to check if the number is prime
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# Function to authenticate and filter prime numbers
def authenticate_and_filter(num_list):
    prime_numbers = []
    for num in num_list:
        if isinstance(num, int):
            if is_prime(num):
                prime_numbers.append(num)
        else:
            print("Non-integer value detected. Please make sure all elements in the list are integers.")

    return prime_numbers