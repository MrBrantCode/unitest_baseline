"""
QUESTION:
Implement the `caesar_cipher` function that encrypts a string using the Caesar cipher with a given shift value. The function should take a string containing only uppercase letters and spaces, and an integer shift value, and return the encrypted string. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def caesar_cipher(string, shift):
    encrypted_string = ""
    for char in string:
        if char == " ":
            encrypted_string += " "
        else:
            ascii_value = ord(char)
            shifted_ascii_value = ascii_value + shift
            if shifted_ascii_value > ord("Z"):
                shifted_ascii_value -= 26
            encrypted_string += chr(shifted_ascii_value)
    return encrypted_string