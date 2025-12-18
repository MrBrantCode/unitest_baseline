"""
QUESTION:
Create a function named `decrypt` that takes a string `enc_string` as input. The function should decrypt the string by adding the ASCII value of each character in the string to a running sum, and then appending the character represented by the current sum to the decrypted string.
"""

def decrypt(enc_string):
    s = 0
    decrypted = ''

    for i in range(len(enc_string)):
        s += ord(enc_string[i])
        decrypted += chr(s)

    return decrypted