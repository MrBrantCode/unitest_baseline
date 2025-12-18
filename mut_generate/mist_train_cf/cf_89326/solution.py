"""
QUESTION:
Write a function named `print_characters` that takes a string of lowercase letters as input, prints each character in the string on a single line, and returns the number of vowels and consonants present in the string.
"""

def entrance(s):
    vowels = 0
    consonants = 0

    for char in s:
        print(char, end=" ")

        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

    print()
    return vowels, consonants