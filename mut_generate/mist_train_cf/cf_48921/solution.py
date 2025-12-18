"""
QUESTION:
Given a string `s` containing alphabetic characters and optional arithmetic or special characters, implement a function `reverse_alphabetic(s)` that returns a new string where only the alphabetic characters are reversed in their positioning, keeping all non-alphabetic characters constant in their original position. The function should handle edge cases where numeric and special characters are intermixed with alphabetic characters, and it should only accept strings consisting of printable ASCII characters.
"""

def reverse_alphabetic(s: str) -> str:
    # Create list with all alphabetic characters reversed
    letters = [c for c in s if c.isalpha()][::-1]

    # Get characters from reversed letter list or original string as necessary
    result = [letters.pop(0) if c.isalpha() else c for c in s]

    # Join all characters into a string
    return ''.join(result)