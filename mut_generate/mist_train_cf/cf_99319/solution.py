"""
QUESTION:
Create a function called `divide_number` that takes a number as input and returns a list of the smallest possible number of 3-digit numbers that represent the original number. The function should handle cases where the original number cannot be divided into equal 3-digit numbers by adding leading zeros to the first part.
"""

def divide_number(number):
    num_digits = len(str(number))
    num_parts = (num_digits - 1) // 3 + 1
    parts = []
    for i in range(num_parts):
        part = number % 1000
        parts.append(part)
        number //= 1000
    parts.reverse()
    parts = [str(part).zfill(3) for part in parts]
    return parts