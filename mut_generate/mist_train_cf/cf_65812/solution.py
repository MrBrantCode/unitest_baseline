"""
QUESTION:
Write a function named `prime_hex_count` that takes a string of hexadecimal digits as input and returns the number of prime hexadecimal digits in the string, doubled if any two prime digits are consecutive. The hexadecimal digits can be 0-9 and A-F (where A-F are always uppercase). Assume the input string is always correct or empty.
"""

def prime_hex_count(hex_input):
    count = 0
    consecutive = False
    prime_hex_values = ["2", "3", "5", "7", "B", "D", "F"]
    for i in range(len(hex_input)):
        if hex_input[i] in prime_hex_values:
            count += 1
            if i > 0 and hex_input[i-1] in prime_hex_values:
                consecutive = True
    return count * 2 if consecutive else count