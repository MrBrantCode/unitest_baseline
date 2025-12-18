"""
QUESTION:
Create a function called `flip_and_convert` that takes a string `s` as input, inverts the characters at even index positions by converting them to their corresponding ASCII values, and leaves the characters at odd index positions untouched.
"""

def flip_and_convert(s: str):
    result = ''
    for i in range(len(s)):
        # Return ASCII for even-indexed characters, original character for odd-indexed ones
        result += str(ord(s[i])) if i % 2 == 0 else s[i]
    return result