"""
QUESTION:
Write a function `count_vowels(sentence)` that takes a string `sentence` as input and returns the number of vowels that occur after a consonant and before another consonant, ignoring any vowels that occur at the beginning or end of a word. The function should be case-insensitive.
"""

def count_vowels(sentence):
    count = 0
    sentence = sentence.lower()
    words = sentence.split()

    for word in words:
        if len(word) > 2:
            for i in range(1, len(word) - 1):
                if (
                    word[i] in "aeiou"
                    and word[i-1] not in "aeiou"
                    and word[i+1] not in "aeiou"
                ):
                    count += 1

    return count