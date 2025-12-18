"""
QUESTION:
Write a function `calculate_product_of_digits` that takes an integer as input and returns the product of its digits. Then, using this function, write a program that finds all numbers in a given list that are divisible by both 3 and 5, and for each number found, prints the number and the product of its digits. 

Restrictions: The input list consists of integers, and the product of digits for a number is calculated by treating each digit as an integer and multiplying them together.
"""

def calculate_product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product