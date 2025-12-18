"""
QUESTION:
Implement a function `compare_strings(s1, s2)` that determines if two strings are equal, ignoring non-alphabetic characters and leading/trailing white spaces, while considering the case of alphabetic characters.
"""

def compare_strings(s1, s2):
    # Remove leading and trailing white spaces
    s1 = s1.strip()
    s2 = s2.strip()

    # Remove non-alphabetic characters
    s1 = ''.join(filter(str.isalpha, s1))
    s2 = ''.join(filter(str.isalpha, s2))

    # Compare the modified strings
    return s1 == s2