"""
QUESTION:
Create a function called `print_characters` that takes a string of lowercase letters as input and prints each character in the string on the same line, separated by a space. The function should also return the number of vowels and consonants in the string.
"""

def print_characters(string):
    vowels = 0
    consonants = 0

    for char in string:
        print(char, end=" ")

        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

    print()
    return vowels, consonants