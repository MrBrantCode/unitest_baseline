"""
QUESTION:
Write a function called `is_narcissistic` that takes an integer as input and returns True if it's a three-digit narcissistic number and False otherwise. A narcissistic number is a non-negative integer of exactly three digits where the sum of the cubes of each digit is equal to the number itself. The function should not rely on any built-in libraries or functions. Use this function to generate a list of all three-digit narcissistic numbers within the range of 100 to 500.
"""

def is_narcissistic(num):
    digits = [int(d) for d in str(num)] # Convert the number to a list of digits
    sum_of_cubes = sum([d**3 for d in digits]) # Sum the cubes of each digit
    return sum_of_cubes == num # Return True if the sum of cubes is equal to the number itself, False otherwise