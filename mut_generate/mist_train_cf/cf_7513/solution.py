"""
QUESTION:
Write a function `count_vowels(line)` that takes a string `line` as input, containing only lowercase letters and spaces, and returns the number of vowels in the line while ignoring any vowels that appear after a consonant and before another vowel. Assume the input string has a maximum length of 1000 characters.
"""

def entrance(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    ignore_vowel = False

    for char in line:
        if char in vowels:
            if not ignore_vowel:
                vowel_count += 1
            ignore_vowel = True
        else:
            ignore_vowel = False

    return vowel_count