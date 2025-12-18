"""
QUESTION:
Write a function `most_vowels_word` that takes a sentence as input and returns the word with the most vowels. The function should ignore punctuation marks when counting vowels. It should not use any built-in functions or methods for counting vowels or manipulating strings. The function should have a time complexity of O(n), where n is the length of the sentence, and a space complexity of O(1).
"""

def most_vowels_word(sentence):
    max_vowels_count = 0
    max_vowels_word = ''
    current_vowels_count = 0
    current_vowels_word = ''

    for c in sentence:
        if c.isalpha():
            if c.lower() in 'aeiou':
                current_vowels_count += 1
                current_vowels_word += c
            else:
                if current_vowels_count > max_vowels_count:
                    max_vowels_count = current_vowels_count
                    max_vowels_word = current_vowels_word
                current_vowels_count = 0
                current_vowels_word = ''
        elif not c.isalnum():
            if current_vowels_count > max_vowels_count:
                max_vowels_count = current_vowels_count
                max_vowels_word = current_vowels_word
            current_vowels_count = 0
            current_vowels_word = ''

    if current_vowels_count > max_vowels_count:
        max_vowels_count = current_vowels_count
        max_vowels_word = current_vowels_word

    return max_vowels_word