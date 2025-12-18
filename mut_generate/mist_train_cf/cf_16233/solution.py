"""
QUESTION:
Write a function `count_unique_substrings` that takes a string as input and returns the number of unique substrings possible without any repeated characters. The input string can contain lowercase letters, uppercase letters, digits, and special characters, and its length will not exceed 1000 characters.
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