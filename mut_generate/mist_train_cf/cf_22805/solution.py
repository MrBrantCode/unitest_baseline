"""
QUESTION:
Write a function `replace_first_letter_with_underscore` that takes a string as input, replaces the first letter of each word with an underscore (_) if the word starts with a consonant, and capitalizes the first letter of each word after replacement. The function should handle words that start with vowels by not replacing the first letter.
"""

def replace_first_letter_with_underscore(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = string.split()
    new_string = ""
    for word in words:
        if word[0].lower() not in vowels:
            new_string += "_" + word[1:].capitalize() + " "
        else:
            new_string += word.capitalize() + " "
    return new_string.strip()