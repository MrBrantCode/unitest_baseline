"""
QUESTION:
Implement a function named `complex_encode` that takes a string `s` and an integer `n` as inputs, and returns an encoded string by shifting each character in `s` to the right by `n` positions, using recursion. The function should handle both lowercase and uppercase letters, digits, and special characters, leaving the latter unchanged. The shift should wrap around for letters and digits, and the function should work for strings of any length, including empty strings.
"""

def complex_encode(s, n):
    if len(s) == 0:
        return s
    else:
        new_char = s[0]
        if new_char.isalpha():
            ascii_offset = ord('A') if new_char.isupper() else ord('a')
            new_char = chr(((ord(new_char) - ascii_offset + n) % 26) + ascii_offset)
        elif new_char.isdigit():
            new_char = str((int(new_char) + n) % 10)
        return new_char + complex_encode(s[1:], n)