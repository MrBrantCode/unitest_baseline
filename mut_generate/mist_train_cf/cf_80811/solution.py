"""
QUESTION:
Create a function named `advanced_encrypt` that accepts a string `s` and an integer `n` as input. The function should produce an encrypted string using a shifted alphabet approach by multiplying the shift by three and shifting `n` positions, while utilizing modulo to handle edge cases. The function should preserve case sensitivity, non-alphabetic elements, special characters, and digits in the final output, and work consistently with both lowercase and uppercase alphabets. The input `n` specifies the dynamic shift count.
"""

def advanced_encrypt(s, n):
    result = ""
    for i in s:
        if i.isalpha():
            shift = 3 * n
            char_code = ord(i) + shift
            if i.isupper():
                result += chr(char_code % 65 % 26 + 65)
            else:
                result += chr(char_code % 97 % 26 + 97)
        else:
            result += i
    return result