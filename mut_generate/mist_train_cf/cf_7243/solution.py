"""
QUESTION:
Write a function `compare_strings` that takes two strings as input, removes leading and trailing white spaces, and then removes all non-alphabetic characters from the strings. The function should compare the modified strings in a case-sensitive manner and return True if they are equal, False otherwise.
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