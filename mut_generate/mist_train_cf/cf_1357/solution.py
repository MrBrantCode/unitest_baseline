"""
QUESTION:
Create a function called `get_lengths` that takes an array of strings as input. Each string in the array should be at least 10 characters long and no more than 30 characters long, should not contain numbers or special characters, and should not start with a vowel. The function should also ignore strings that have a repeated substring of at least length 4. The function should return an array of lengths of all valid strings. If no valid strings are found, return an empty array.
"""

def get_lengths(strings):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lengths = []
    for string in strings:
        if (10 <= len(string) <= 30 and 
            not any(char.isdigit() or not char.isalnum() for char in string) and 
            string[0].lower() not in vowels and 
            not any(string.count(string[i:i+4]) > 1 for i in range(len(string) - 3))):
            lengths.append(len(string))
    return lengths