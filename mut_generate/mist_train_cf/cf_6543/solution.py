"""
QUESTION:
Write a Python function named `is_prime` that checks if a given positive integer is prime or not. The function should use recursion and have a time complexity of O(sqrt(n)). Additionally, create a function named `get_input` that ensures the input is a positive integer greater than 10 and less than or equal to 100.
"""

import math

def is_prime(n, divisor=2):
    if n < 2:
        return False
    if divisor <= math.sqrt(n):
        if n % divisor == 0:
            return False
        return is_prime(n, divisor+1)
    return True

def get_input():
    while True:
        try:
            num = int(input("Enter a positive integer greater than 10 and less than or equal to 100: "))
            if num > 10 and num <= 100:
                return num
            else:
                print("Input must be greater than 10 and less than or equal to 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")