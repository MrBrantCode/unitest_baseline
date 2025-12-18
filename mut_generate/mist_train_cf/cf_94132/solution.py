"""
QUESTION:
Implement a function `count_unique_substrings` that calculates the number of unique substrings without repeated characters in a given string of up to 1000 characters, containing lowercase letters, uppercase letters, digits, and special characters.
"""

def count_unique_substrings(string):
    unique_substrings = set()

    for i in range(len(string)):
        substring = ''
        for j in range(i, len(string)):
            if string[j] in substring:
                break
            substring += string[j]
            unique_substrings.add(substring)

    return len(unique_substrings)