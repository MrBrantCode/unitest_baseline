"""
QUESTION:
Create a function called `process_string` that takes a string as input and returns a new string. The function should remove all alphabetic characters from the input string, replace each digit with its binary representation (without the '0b' prefix), and replace all non-alphanumeric characters with an asterisk (*).
"""

def process_string(input_string):
    result = ''
    for ch in input_string:
        if ch.isalpha():
            continue
        elif ch.isdigit():
            binary = bin(int(ch))[2:]  # Convert to binary and discard '0b' prefix
            result += str(binary)
        else:
            result += '*'
    return result