"""
QUESTION:
Create a function named `process_text` that takes a string of text input and performs the following tasks: 

It must return a dictionary containing the total number of each vowel (both in uppercase and lowercase). 
It must return the total number of vowels and the total number of consonants separately. 
It must determine if the total number of vowels is odd or even.

Note: Non-alphabet characters in the input string should not be counted as vowels or consonants.
"""

def process_text(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    total_vowels = 0
    total_consonants = 0

    for character in text:
        if character in vowels:
            vowel_count[character] += 1
            total_vowels += 1
        elif character.isalpha():
            total_consonants += 1

    result = {
        'vowel_counts': vowel_count,
        'total_vowels': total_vowels,
        'total_consonants': total_consonants,
        'vowel_parity': 'odd' if total_vowels % 2 != 0 else 'even'
    }
    
    return result