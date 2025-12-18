"""
QUESTION:
Create a function named char_count that takes a string s as input and returns a dictionary with the count of vowels, consonants, and special characters in the string. The function should be case-insensitive and consider 'y' as a vowel only when it appears at the end of the string. The function should ignore non-alphabetic characters as special characters.
"""

def char_count(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count_vowels = 0
    count_consonants = 0
    count_specials = 0
    s = s.lower()

    for i in s:
        if i.isalpha():
            if i in vowels or (i == 'y' and s.endswith('y')):
                count_vowels += 1
            else:
                count_consonants += 1
        else:
            count_specials += 1

    return {'Vowels': count_vowels, 'Consonants': count_consonants, 'Special characters': count_specials}