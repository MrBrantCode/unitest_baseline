"""
QUESTION:
Develop a function named `transpose_string` that takes two parameters: a string `s` and an integer `n`, representing the number of characters to transpose. The function should transpose the string `s` to the right by `n` characters in place, without allocating additional memory. If `n` is negative, the function should transpose the string to the left. The function should handle transposition values that exceed the length of the string by wrapping around the string. The function should validate the input to ensure it is a non-empty string and an integer, and raise an exception if the input is invalid. The function should be able to handle multi-byte characters, special symbols, and numbers.
"""

def transpose_string(s, n):
    if not isinstance(s, str) or not isinstance(n, int):
        raise Exception("Invalid input. Expected string and integer.")
    if len(s) < 1:
        raise Exception("String cannot be empty.")
    n = n % len(s) 
    if n < 0: 
        n = n + len(s)
    return s[-n:]+s[:-n] 