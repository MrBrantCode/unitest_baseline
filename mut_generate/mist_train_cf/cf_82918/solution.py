"""
QUESTION:
Implement a function `binary_to_octal` that takes a binary numeral string as input and returns its corresponding octal form as a string. The function should not include the '0o' prefix in the output.
"""

def binary_to_octal(n: str) -> str:
    return oct(int(n, 2))[2:]