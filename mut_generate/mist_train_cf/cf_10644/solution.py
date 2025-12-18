"""
QUESTION:
Write a function `binary_to_decimal(binary)` that takes a string of binary digits as input and returns its equivalent decimal number. The function should handle binary numbers up to 32 bits in length and include error handling for invalid input.
"""

def binary_to_decimal(binary):
    try:
        decimal = int(binary, 2)
        return decimal
    except ValueError:
        print("Invalid input. Please enter a binary number.")
        return None