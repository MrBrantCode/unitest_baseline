"""
QUESTION:
Write a function `find_longest_vowel_consonant_word(word_list)` that takes a list of words as input and returns the longest word that starts with a vowel and ends with a consonant. The function should ignore any words that contain numbers or special characters. If no such word exists, it should return None.
"""

def find_longest_vowel_consonant_word(word_list):
    longest_word = None

    for word in word_list:
        if word.isalpha() and word[0].lower() in "aeiou" and word[-1].lower() not in "aeiou":
            if longest_word is None or len(word) > len(longest_word):
                longest_word = word

    return longest_word