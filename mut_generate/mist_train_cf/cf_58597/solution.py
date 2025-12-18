"""
QUESTION:
Write a function `rearrange_string(s)` that takes a string `s` consisting of lowercase letters and special characters. The function should segregate the vowels, consonants, and special characters in the string, ordering vowels and consonants alphabetically while leaving the special characters in their original positions. If a character position has both a vowel and a consonant, it should be considered a consonant. The function should return the rearranged string.
"""

def rearrange_string(s):
    vowels = []
    consonants = []
    other_chars_loc = []
    s_list = list(s)
    for i in range(len(s)):
        if s[i] in 'aeiou':
            vowels.append(s[i])
        elif s[i].isalpha():
            consonants.append(s[i])
        else:
            other_chars_loc.append(i)
    sorted_vowels = iter(sorted(vowels))
    sorted_consonants = iter(sorted(consonants))
    for i in range(len(s)):
        if i not in other_chars_loc:
            if s[i] in 'aeiou':
                s_list[i] = next(sorted_vowels)
            else:
                s_list[i] = next(sorted_consonants)
    return ''.join(s_list)