"""
ORIGINAL QUESTION:
Write a function called `replace_vowels` that takes a string as input, replaces all vowels with underscores while preserving the original case, and removes consecutive duplicate vowels. The input string only contains alphabetic characters and punctuation marks, with no leading or trailing spaces.
"""

def replace_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    output_string = ""
    prev_vowel = False

    for char in input_string:
        if char in vowels:
            if not prev_vowel:
                output_string += "_"
            prev_vowel = True
        else:
            output_string += char
            prev_vowel = False

    return output_string