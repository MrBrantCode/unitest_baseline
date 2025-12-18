"""
QUESTION:
Create a function `compare_strings` that takes two string parameters. The function should compare the two strings and return a list of characters that are vowels in one string but not the other. The comparison should be case-insensitive and consider only the characters 'a', 'e', 'i', 'o', 'u', and their uppercase counterparts as vowels.
"""

def compare_strings(string1, string2):
    differences = []

    string1 = string1.lower()
    string2 = string2.lower()

    for char in string1:
        if char.lower() in 'aeiou' and char not in string2:
            differences.append(char)

    for char in string2:
        if char.lower() in 'aeiou' and char not in string1:
            differences.append(char)

    return differences