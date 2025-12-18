"""
QUESTION:
Write a function `calculate_cone_volume` that takes no arguments and prompts the user for the height and radius of a cone. The function should calculate the volume of the cone only if the height and radius are prime numbers less than 50, and print the result. If the inputs are not valid integers or do not meet the prime number condition, it should print an error message.
"""

import math

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def calculate_cone_volume():
    try:
        height = int(input("Enter the height of the cone: "))
        radius = int(input("Enter the radius of the cone: "))

        if is_prime(height) and is_prime(radius) and height < 50 and radius < 50:
            volume = (math.pi * radius * radius * height)/3
            print("The volume of the cone is: ", volume)
        else:
            print("The height and radius should be prime numbers less than 50.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")