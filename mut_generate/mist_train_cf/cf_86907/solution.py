"""
QUESTION:
Create a function named `get_lengths` that takes an array of strings and returns an array of their lengths. Each string should be between 10 and 30 characters long, contain only letters, and not start with a vowel. Additionally, strings with a repeated substring of at least length 4 should be ignored. Return an empty array if no valid strings are found.
"""

def get_lengths(strings):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lengths = []
    for string in strings:
        if (10 <= len(string) <= 30 and 
            string.isalpha() and 
            string[0].lower() not in vowels and 
            all(string.count(substring) == 1 for substring in (string[i:i+4] for i in range(len(string) - 3)))):
            lengths.append(len(string))
    return lengths