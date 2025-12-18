"""
QUESTION:
Generate a string of length `n` and `m` with characters that have odd counts and even counts. The string should contain only lowercase English letters and must be divided into two halves. Each character in the first half of the string must occur an odd number of times, and each character in the second half of the string must occur an even number of times. If there are multiple valid strings, return any of them. The function should be named `oddEvenString` and take two integers `n` and `m` as input, where `1 <= n, m <= 500`.
"""

def generate_string(n, m):
    if n % 2 == 1:
        first_half = chr(97) * n
        second_half = chr(98) * m 
    else:
        first_half = chr(97) * (n - 1) + chr(98)
        second_half = chr(99) * m
    return first_half + second_half