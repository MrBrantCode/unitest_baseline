"""
QUESTION:
Create a function called `print_characters` that takes a string of lowercase letters as input. The function should print each character of the string on a single line and return the total count of vowels present in the string.
"""

def print_characters(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for char in string:
        print(char)
        if char in vowels:
            vowel_count += 1
    return vowel_count