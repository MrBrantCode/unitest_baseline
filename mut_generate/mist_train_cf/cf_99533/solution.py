"""
QUESTION:
Create a function called `find_first_prime` to find the first prime number greater than 50 from a given list of numbers. The function should take a list of integers as input and return the first prime number greater than 50. If no such number exists in the list, the function should return a suitable message or value. The input list may contain any integers (positive, negative, or zero), but the function should only consider numbers greater than 50 when searching for a prime number.
"""

def find_first_prime(numbers):
    # function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in numbers:
        if num > 50 and is_prime(num):
            return num
    return "No prime number greater than 50 found in the list"