"""
QUESTION:
Write a function `binary_to_decimal(binaryNum)` that takes a string of binary digits as input and returns its equivalent decimal value. The function should handle cases where the input string contains non-binary characters by returning an error message.
"""

def binary_to_decimal(binaryNum):
    try:
        # Use int() function in python with 2 as base argument to convert binary string into decimal.
        # int(string, base)
        return int(binaryNum, 2)
    except ValueError:
        # If binaryNum is not a valid binary number, int() function will raise a ValueError.
        # Return error message in case of exception
        return "Invalid binary input"