"""
QUESTION:
Implement a function `solve_problem` that takes an encrypted string as input, where the encryption is done using a Caesar cipher with a shift equal to the length of the input string. The function should decrypt the input string, reverse it, and then prepend "Hola " to the result. The function should handle both uppercase and lowercase characters in the input string.
"""

def solve_problem(input_str):
    shift = len(input_str)
    result = ""
    for char in input_str:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return "Hola " + result[::-1]