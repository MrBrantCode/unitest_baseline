"""
QUESTION:
Write a function `analyze_string(s)` that calculates the number of vowels, consonants, and special characters in a given string `s`, ignoring white spaces and numbers. The function should also calculate the frequency of vowels and consonants in the string. Special characters are defined as any characters that are not vowels, consonants, or numbers.
"""

def analyze_string(s):
    s = s.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    num_vowels = 0
    num_consonants = 0
    num_special = 0
    vowel_freq = {}
    consonants_freq = {}

    for i in s:
        if i in vowels:
            num_vowels += 1
            if i in vowel_freq:
                vowel_freq[i] += 1
            else:
                vowel_freq[i] = 1
        elif i in consonants:
            num_consonants += 1
            if i in consonants_freq:
                consonants_freq[i] += 1
            else:
                consonants_freq[i] = 1
        elif i.isalnum() == False and i != ' ':
            num_special += 1

    return {
        "num_vowels": num_vowels,
        "num_consonants": num_consonants,
        "num_special": num_special,
        "vowel_freq": vowel_freq,
        "consonant_freq": consonants_freq
    }