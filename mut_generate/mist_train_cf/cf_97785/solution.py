"""
QUESTION:
Write a function named `divide_number` that takes a positive integer as input and returns a list of strings, where each string is a 3-digit number. The numbers in the list should be the smallest possible 3-digit numbers that, when concatenated, form the original number. If the original number cannot be divided into equal 3-digit numbers, the first number in the list should be padded with leading zeros to a length of 3.
"""

def divide_number(number):
    # Calculate the number of 3-digit numbers needed to represent the number
    num_digits = len(str(number))
    num_parts = (num_digits - 1) // 3 + 1
    # Divide the number into 3-digit parts
    parts = []
    for i in range(num_parts):
        part = number % 1000
        parts.append(part)
        number //= 1000
    # Reverse the list of parts and convert them to strings
    parts.reverse()
    parts = [str(part).zfill(3) for part in parts]
    # Return the list of 3-digit parts
    return parts