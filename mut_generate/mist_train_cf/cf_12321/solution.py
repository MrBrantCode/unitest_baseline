"""
QUESTION:
Create a function `binary_to_hexadecimal(binary)` that takes a binary string `binary` as input and returns its equivalent hexadecimal representation as a string. The function should not use any built-in functions or libraries for the conversion. The input binary string can be of any length, but the function should handle cases where the length is not a multiple of 4 by adding leading zeros.
"""

def binary_to_hexadecimal(binary):
    # Initialize hexadecimal dictionary
    hex_dict = {
        0: '0', 1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B',
        12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    
    # Initialize hexadecimal string
    hexadecimal = ""

    # Determine the number of digits and groups of 4 digits
    binary_length = len(binary)
    groups = binary_length // 4

    # Add leading zeros if necessary
    if binary_length % 4 != 0:
        binary = "0" * (4 - binary_length % 4) + binary
        groups += 1

    # Convert groups of 4 digits to hexadecimal
    for i in range(groups):
        # Get the next group of 4 digits
        group = binary[i * 4: (i + 1) * 4]
        
        # Convert the group to decimal
        decimal = 0
        for j in range(4):
            decimal += int(group[j]) * 2 ** (3 - j)
        
        # Convert decimal to hexadecimal and append to the result
        hexadecimal += hex_dict[decimal]

    return hexadecimal