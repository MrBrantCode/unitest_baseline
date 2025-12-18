"""
QUESTION:
Write a function called `hex_to_binary(hex_string)` that takes a hexadecimal string as input and returns the corresponding binary string. The function should return an error message if the input string contains any invalid hexadecimal characters.
"""

def hex_to_binary(hex_string):
    binary_string = ""
    for char in hex_string:
        if char == "0":
            binary_string += "0000"
        elif char == "1":
            binary_string += "0001"
        elif char == "2":
            binary_string += "0010"
        elif char == "3":
            binary_string += "0011"
        elif char == "4":
            binary_string += "0100"
        elif char == "5":
            binary_string += "0101"
        elif char == "6":
            binary_string += "0110"
        elif char == "7":
            binary_string += "0111"
        elif char == "8":
            binary_string += "1000"
        elif char == "9":
            binary_string += "1001"
        elif char == "A":
            binary_string += "1010"
        elif char == "B":
            binary_string += "1011"
        elif char == "C":
            binary_string += "1100"
        elif char == "D":
            binary_string += "1101"
        elif char == "E":
            binary_string += "1110"
        elif char == "F":
            binary_string += "1111"
        elif char == "a":
            binary_string += "1010"
        elif char == "b":
            binary_string += "1011"
        elif char == "c":
            binary_string += "1100"
        elif char == "d":
            binary_string += "1101"
        elif char == "e":
            binary_string += "1110"
        elif char == "f":
            binary_string += "1111"
        else:
            return "Invalid Hexadecimal Character"  # Return an error message if invalid character encountered
    return binary_string