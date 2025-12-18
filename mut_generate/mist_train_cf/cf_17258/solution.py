"""
QUESTION:
Write a function `count_characters` that takes a string as input, counts the number of vowels, consonants, digits, special characters (any character that is not a letter or a digit), and spaces in the string, and returns these counts. The function should handle both uppercase and lowercase characters, non-ASCII characters, and any other characters.
"""

def count_characters(string):
    vowels_count = 0
    consonants_count = 0
    digits_count = 0
    special_chars_count = 0
    spaces_count = 0

    for char in string:
        if char.lower() in 'aeiou':
            vowels_count += 1
        elif char.isalpha():
            consonants_count += 1
        elif char.isdigit():
            digits_count += 1
        elif char.isspace():
            spaces_count += 1
        else:
            special_chars_count += 1

    return vowels_count, consonants_count, digits_count, special_chars_count, spaces_count