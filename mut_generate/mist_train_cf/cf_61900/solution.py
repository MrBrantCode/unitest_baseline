"""
QUESTION:
Create a function named `encrypt` that takes a string `s` and an integer `rot` as inputs, and returns an encrypted string. The function should shift alphabet characters by the square of `rot` places, preserving case, and leaving non-alphabetic characters unchanged. If the shift exceeds 26, it should wrap around the alphabet.
"""

def encrypt(s, rot):
    # Create a callback for offset calculation
    def offset_calc(c, a):
        return chr((ord(c) - a + (rot * rot) % 26) % 26 + a)
        
    # Iterate through the string and translate alphabetic characters
    return ''.join(
        offset_calc(c, ord('a')) if c.islower() else offset_calc(c, ord('A')) 
        if c.isupper() else c for c in s)