"""
QUESTION:
Write a function `max_vowel_word` that takes a sentence as input and returns the word with the most vowels. The function should not use any built-in functions or methods for counting vowels or manipulating strings, and it should have a time complexity of O(n), where n is the length of the sentence, and a space complexity of O(1).
"""

def max_vowel_word(sentence):
    max_vowel_count = 0
    max_vowel_word = ""
    current_word = ""
    vowel_count = 0

    for c in sentence:
        if c.isalpha():
            current_word += c
        if (not c.isalnum() or c == sentence[-1]) and current_word:
            if vowel_count > max_vowel_count:
                max_vowel_count = vowel_count
                max_vowel_word = current_word
            current_word = ""
            vowel_count = 0
        if c in 'aeiouAEIOU':
            vowel_count += 1

    return max_vowel_word