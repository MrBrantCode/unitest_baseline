"""
QUESTION:
Write a function named `inverse_even_characters` that takes a string `s` as input and returns a new string where characters at even indices are reversed and characters at odd indices remain in their original order.
"""

def inverse_even_characters(s: str) -> str:
    # Get characters at even indices and reverse
    even_chars = s[::2][::-1]
    # Get characters at odd indices
    odd_chars = s[1::2]
    # Initialize output string
    output = ""
    # Iterate over the lengths of even and odd parts
    for i in range(max(len(even_chars), len(odd_chars))):
        # Add next character from even_chars list if available
        if i < len(even_chars):
            output += even_chars[i]
        # Add next character from odd_chars list if available
        if i < len(odd_chars):
            output += odd_chars[i]
    return output