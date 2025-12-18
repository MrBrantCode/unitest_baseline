"""
QUESTION:
Create a function `integer_to_string(n)` that takes an input `n` and returns its string representation. The function must validate that `n` is a non-negative integer and handle numbers up to 10**18. If `n` is not an integer, or is negative, or exceeds 10**18, return an error message. The function cannot use built-in string conversion functions like `str()`.
"""

def integer_to_string(n):
    if not isinstance(n, int):
        return "Error: input is not an integer."
    if n < 0:
        return "Error: input must be a non-negative integer."
    if n > 10**18:
        return "Error: input is too large."
    result = ''
    if n == 0:
        return chr(ord('0'))
    while n > 0:
        digit = n % 10
        result = chr(ord('0') + digit) + result
        n = n // 10
    return result