"""
QUESTION:
Design a function named "cipher" that accepts a string and returns the encrypted string. The encryption should be done by shifting each alphabet in the string three positions to the right using the modulo operation to handle boundary scenarios. The function should respect case sensitivity, include non-alphabetic characters in the output, and consider both lowercase and uppercase alphabets during rotation. The function should not modify non-alphabetic characters.
"""

def cipher(s):
    result = ""
    for char in s:
        # Check if the character is an alphabet
        if char.isalpha():
            # calculate shift amount
            shift = 3
            # handle lower case letters
            if char.islower():
                # compute the new alphabet index after shift and wrap around using modulo
                # ord('a') gives the ASCII value of 'a'. For lower case alphabets, 'a' is considered to be at position 0
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                # similarly handle uppercase letters
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # for non-alphabets, simply append the character as it is
            result += char
    return result