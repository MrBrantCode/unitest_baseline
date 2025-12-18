"""
QUESTION:
Create a function `get_square_area()` that takes no arguments. Inside this function, continuously prompt the user for a side length until a valid input is provided, where a valid input is a positive integer greater than zero that is a prime number. Once a valid input is obtained, calculate the area of the square by squaring the side length and return the calculated area.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_square_area():
    while True:
        side_length = input("Enter the side length of the square: ")
        try:
            side_length = int(side_length)
            if side_length > 0 and is_prime(side_length):
                return side_length ** 2
            else:
                print("Invalid input. Please enter a positive integer greater than zero and a prime number.")
        except ValueError:
            print("Invalid input. Please enter a positive integer greater than zero and a prime number.")