"""
QUESTION:
Develop a function named `count_vowels_and_consonants` that takes a sequence of alphabetic characters as input. The function should return the total count of vowel sounds, the total count of vowel letters, and the unique count of consonant letters. Consider 'y' as a vowel only when it is not followed by another vowel, and ignore special characters or numbers during the consonant count. Both uppercase and lowercase characters should be considered.
"""

def count_vowels_and_consonants(seq):
    vowels = 'aeiou'
    vowels_y = 'aeiouy'
    
    seq = seq.lower() 
    
    vowel_sounds = 0
    vowel_letters = 0
    consonants = set()

    i = 0
    while(i < len(seq)):
        if seq[i] in vowels_y:
            vowel_letters += 1
            if seq[i] == 'y' and i + 1 < len(seq) and seq[i+1] in vowels_y:
                pass
            else:
                vowel_sounds += 1
        elif seq[i].isalpha():
            consonants.add(seq[i])

        i += 1

    return vowel_sounds, vowel_letters, len(consonants)