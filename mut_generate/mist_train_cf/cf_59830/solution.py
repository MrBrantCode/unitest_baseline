"""
QUESTION:
Write a Python function `separate_and_cross_reference_strings` that takes one or two strings as input and returns a dictionary with the vowels and consonants separated for each string, as well as the shared vowels and consonants between the two strings if a second string is provided. The function should handle strings composed entirely of non-alphabetic characters, strings that only contain vowels or consonants, empty strings, and strings with Unicode alphabetic characters.
"""

def separate_and_cross_reference_strings(string1, string2=None):
    vowels = set('aeiouAEIOU')
    
    def process_string(s):
        s_vowels = set()
        s_consonants = set()
        for char in s:
            if char.isalpha():
                if char in vowels:
                    s_vowels.add(char)
                else:
                    s_consonants.add(char)
        return s_vowels, s_consonants

    s1_vowels, s1_consonants = process_string(string1)
    
    if string2 is not None:
        s2_vowels, s2_consonants = process_string(string2)
        shared_vowels = s1_vowels & s2_vowels
        shared_consonants = s1_consonants & s2_consonants
    else:
        s2_vowels, s2_consonants, shared_vowels, shared_consonants = set(), set(), set(), set()

    return {
        'string1': {'vowels': s1_vowels, 'consonants': s1_consonants},
        'string2': {'vowels': s2_vowels, 'consonants': s2_consonants},
        'shared': {'vowels': shared_vowels, 'consonants': shared_consonants},
    }