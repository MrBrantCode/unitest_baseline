"""
QUESTION:
Create a function named `inverse_even_characters` that takes a string `s` as input. The function should return a transformed string where characters at even indices (0-based indexing) are reversed in order, while characters at odd indices remain in their original order.
"""

def inverse_even_characters(s: str):
    even_chars = [s[i] for i in range(len(s)) if i % 2 == 0]
    reversed_even = even_chars[::-1]
    result = ''
    j = 0
    for i in range(len(s)):
        if i % 2 == 0:
            result += reversed_even[j]
            j += 1
        else:
            result += s[i]
    return result