"""
QUESTION:
Create a function `generate_binary` that generates a binary representation of a given positive integer without any consecutive 1s. The function should use a loop to generate the binary representation and must not use any built-in functions or libraries to convert decimal to binary. The function should handle input numbers up to 10^6 and output the binary representation as a string.
"""

def generate_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2

    # Remove consecutive 1s if any
    binary = binary.replace("11", "10")
    return binary