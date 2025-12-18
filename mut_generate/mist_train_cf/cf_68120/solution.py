"""
QUESTION:
Implement a function named `advanced_encrypt` that takes a string `s` and an integer `n` as input, and returns the string encrypted using a shifted alphabet formula. The shift should be executed by tripling and displacing `n` positions, while applying the modulo operator to handle edge cases efficiently. The function should maintain case sensitivity, honor non-alphabetic symbols, special characters, and integers in the final output, and demonstrate consistency with both lowercase and uppercase alphabets.
"""

def advanced_encrypt(s, n):
    def shift(c):
        order = ord(c)
        if 65 <= order <= 90:  # Capital Letters in ASCII
            return chr(((order - 65 + n*3) % 26) + 65)
        elif 97 <= order <= 122:   # Small Letters in ASCII
            return chr(((order - 97 + n*3) % 26) + 97)
        return c  # Non-alphabetic characters

    return ''.join(map(shift, s))