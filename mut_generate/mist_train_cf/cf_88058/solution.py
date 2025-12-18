"""
QUESTION:
Write a function `check_vowels(sentence)` that takes a sentence as input and returns `True` if all vowels not in words starting with a vowel are followed by a consonant that is not 'y' or a silent letter. Return `False` otherwise. Assume vowels are 'a', 'e', 'i', 'o', 'u' (both uppercase and lowercase), and silent letters are defined as letters not pronounced in a word.
"""

def check_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    words = sentence.lower().split()

    for i in range(len(words)):
        word = words[i]
        if word[0] in vowels:
            continue
        for j in range(1, len(word)):
            if word[j] in vowels:
                if word[j-1] in consonants and word[j-1] != 'y':
                    continue
                else:
                    return False

    return True