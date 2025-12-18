"""
QUESTION:
Write a function called `enhanced_char_count` that takes a string `s` as input and returns a dictionary containing the counts and frequencies of letters, digits, and special characters in the string, as well as the characters with the highest and lowest frequencies. The dictionary should have the following structure: 
- 'Letters' should be a dictionary containing 'Vowels' and 'Consonants' dictionaries with character frequencies.
- 'Digits' should be a dictionary with digit frequencies.
- 'Special characters' should be an integer count of special characters.
- 'Highest frequency' and 'Lowest frequency' should be dictionaries containing characters with the highest and lowest frequencies, respectively.

The function should handle both lowercase and uppercase characters, and consider only the characters in the English alphabet and digits 0-9 as valid characters. All other characters should be counted as special characters.
"""

def enhanced_char_count(s):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    letters = vowels + consonants
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>/?`~"
    digit = "0123456789"
    vowels_freq = {}
    consonants_freq = {}
    digits = {}
    special = 0
    for char in s.lower():
        if char in vowels:
            vowels_freq[char] = vowels_freq.get(char,0)+1
        elif char in consonants:
            consonants_freq[char] = consonants_freq.get(char,0)+1
        elif char in digit:
            digits[char] = digits.get(char,0)+1
        elif char in special_characters: 
            special += 1

    freqs = vowels_freq.copy()
    freqs.update(consonants_freq)
    freqs.update(digits)

    highest_frequency = {k:v for k,v in freqs.items() if v == max(freqs.values())}
    lowest_frequency = {k:v for k,v in freqs.items() if v == min(freqs.values())}

    result = {'Letters': {'Vowels': vowels_freq, 'Consonants': consonants_freq}, 
              'Digits': digits, 'Special characters': special, 
              'Highest frequency': highest_frequency, 
              'Lowest frequency': lowest_frequency}
    
    return result