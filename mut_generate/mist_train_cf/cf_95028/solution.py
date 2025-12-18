"""
QUESTION:
Design a function `concatenate_strings` that takes two strings as input, concatenates the alphabetical characters from both strings, removes duplicates, and returns the result in alphabetical order. The function should ignore non-alphabetical characters and consider only the lowercase versions of the alphabetical characters.
"""

def concatenate_strings(string1, string2):
    # Extract alphabetical characters from both strings
    alpha_chars1 = [char.lower() for char in string1 if char.isalpha()]
    alpha_chars2 = [char.lower() for char in string2 if char.isalpha()]

    # Remove duplicates from both lists
    alpha_chars1 = list(set(alpha_chars1))
    alpha_chars2 = list(set(alpha_chars2))

    # Concatenate the two lists and sort them alphabetically
    result = sorted(alpha_chars1 + alpha_chars2)

    # Join the characters into a string and return it
    return ''.join(result)