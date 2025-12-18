"""
QUESTION:
Write a function `count_vowels(line)` that takes a string of lowercase letters and spaces as input, counts the number of vowels, and ignores any vowels that appear after a consonant and before another vowel.
"""

def count_vowels(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    previous_was_vowel = False

    for char in line:
        if char in vowels:
            if not previous_was_vowel:
                vowel_count += 1
            previous_was_vowel = True
        else:
            previous_was_vowel = False
    
    return vowel_count