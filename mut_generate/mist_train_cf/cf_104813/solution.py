"""
QUESTION:
Write a function named `convert_to_binary` that takes a string input representing a decimal number and returns its binary representation as a string. The input number can be up to 10 digits long and can be positive or negative. If the input string does not represent a valid decimal number, the function should return "Error: Invalid input, please enter a valid number".
"""

def convert_to_binary(number):
    try:
        number = int(number)

        if number < 0:
            binary = bin(number & 0xffffffff)[2:]
        else:
            binary = bin(number)[2:]

        return binary
    except ValueError:
        return "Error: Invalid input, please enter a valid number"