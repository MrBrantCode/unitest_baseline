"""
QUESTION:
Write a function `check_vowels(sentence)` that checks if all vowels in a sentence are followed by a consonant (excluding 'y') and the consonant is not silent. The function should ignore vowels in words that start with a vowel. The function should return True if the conditions are met and False otherwise. The function should handle both uppercase and lowercase letters and assume that silent letters are 'h' in 'ghost' or 'b' in 'subtle'. Vowels include 'a', 'e', 'i', 'o', and 'u'.
"""

def check_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    silent_letters = ['ghost', 'subtle']
    words = sentence.lower().split()

    for i in range(len(words)):
        word = words[i]
        if word[0] in vowels:
            continue
        for j in range(1, len(word)):
            if word[j] in vowels:
                if word[j-1] in consonants and word[j-1] != 'y' and word[j-1:j+1] not in silent_letters:
                    continue
                else:
                    return False

    return True