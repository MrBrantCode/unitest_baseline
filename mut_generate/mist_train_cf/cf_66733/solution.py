"""
QUESTION:
Define a function `compare_strings(string1, string2)` that compares two input strings based on their alphabetical order and lengths, considering the following rules:
- Uppercase and lowercase alphabets are treated as equal (case-insensitive).
- Non-letter characters are compared based on their ASCII values.
- If either string is empty or contains only spaces, the non-empty or non-space string comes first in alphabetical order. If both are empty or contain only spaces, they are considered equal.
- The function should return a string indicating which input string comes first in alphabetical order or if they are equal.
"""

def entrance(string1, string2):
    string1, string2 = string1.strip(), string2.strip()

    # Empty strings or strings containing only spaces are regarded as lowest possible value
    if not string1 and not string2:
        return "The strings are equal."
    elif not string1:
        return "String 2 comes first alphabetically."
    elif not string2:
        return "String 1 comes first alphabetically."

    # Compare length of both strings
    if len(string1) < len(string2):
        return "String 1 comes first alphabetically."
    elif len(string1) > len(string2):
        return "String 2 comes first alphabetically."
    else:
        # Compare string letters
        for c1, c2 in zip(string1.lower(), string2.lower()):
            if ord(c1) < ord(c2):
                return "String 1 comes first alphabetically."
            elif ord(c1) > ord(c2):
                return "String 2 comes first alphabetically."

    return "The strings are equal."