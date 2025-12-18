"""
QUESTION:
Write a function called `divide_by_five` that takes a range of numbers as input, computes their quotients and remainders when divided by 5, and returns the highest remainder among them. The function should iterate through each number in the range, calculate the quotient and remainder using integer division (//) and modulus (%) operators, and keep track of the highest remainder seen so far.
"""

def divide_by_five(numbers):
    highest_remainder = 0
    for num in numbers:
        remainder = num % 5
        if remainder > highest_remainder:
            highest_remainder = remainder
    return highest_remainder