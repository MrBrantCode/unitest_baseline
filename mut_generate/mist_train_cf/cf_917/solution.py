"""
QUESTION:
Create a function named `remove_leading_zeros` that takes a string of up to 100 alphanumeric characters as input. The function should remove leading zeros if they are followed by a non-zero digit and also remove any leading zeros that are followed by another zero. The function should handle both uppercase and lowercase letters and return the resulting string.
"""

def remove_leading_zeros(string):
    if string == "":
        return ""

    # Initialize variables
    result = ""
    i = 0
    length = len(string)

    # Remove leading zeros
    while i < length and string[i] == '0':
        i += 1

    # Copy the remaining characters to the result
    while i < length:
        # Remove leading zeros followed by another zero
        if string[i] == '0' and i + 1 < length and string[i + 1] == '0':
            i += 1
        # Remove leading zeros followed by a non-zero digit
        elif string[i] == '0' and i + 1 < length and string[i + 1].isdigit() and string[i + 1] != '0':
            i += 1
        else:
            result += string[i]
            i += 1

    return result