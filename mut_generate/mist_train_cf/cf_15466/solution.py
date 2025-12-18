"""
QUESTION:
Write a function `count_unique_vowels(sentence)` that counts the number of unique vowels in a sentence. A vowel is considered only if it occurs after a consonant and before another consonant. Vowels at the beginning or end of a word are ignored. The solution must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the sentence.
"""

def count_unique_vowels(sentence):
    vowels = set('aeiou')
    unique_vowels = set()
    prev_consonant = False

    for i in range(1, len(sentence)-1):
        if sentence[i] in vowels:
            if prev_consonant and sentence[i+1] not in vowels and (i + 1 == len(sentence) - 1 or sentence[i+2] not in vowels):
                unique_vowels.add(sentence[i])
            prev_consonant = False
        elif sentence[i].isalpha() and sentence[i] not in vowels:
            if i + 1 < len(sentence) and sentence[i+1] in vowels:
                prev_consonant = True

    return len(unique_vowels)