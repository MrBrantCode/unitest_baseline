"""
QUESTION:
Create a function `count_substrings(sentence)` that takes a string of lowercase letters as input. The function should count the number of non-overlapping substrings of length 4 in the sentence, where each substring starts with a vowel, followed by any two characters, and ends with a consonant. Return the count of such substrings. Assume the input sentence does not contain punctuation or special characters.
"""

def count_substrings(sentence):
    counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(x) for x in range(ord('a'), ord('z')+1) if chr(x) not in vowels]

    for i in range(len(sentence) - 3):
        if sentence[i] in vowels:
            if sentence[i+1] != '' and sentence[i+2] != '':
                if sentence[i+3] in consonants:
                    counter += 1

    return counter