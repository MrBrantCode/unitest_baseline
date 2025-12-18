"""
QUESTION:
Write a function `binary_to_octal` that takes an array of binary strings as input and returns an array of their corresponding octal integer equivalents.
"""

def binary_to_octal(binary_arr):
    octal_arr = []
    for binary in binary_arr:
        # Convert binary to integer then to octal
        octal = oct(int(binary, 2))[2:]  # [2:] is used to remove '0o' from the start
        octal_arr.append(int(octal))
    return octal_arr