"""
QUESTION:
Write a function `find_longest_vowel_consonant_word` that takes a list of words as input and returns the longest word that starts with a vowel and ends with a consonant. The function should ignore any words that contain numbers or special characters. If no such word exists, it should return None.
"""

def find_longest_vowel_consonant_word(word_list):
    longest_word = None

    for word in word_list:
        # Check if word starts with a vowel and ends with a consonant
        if word[0].lower() in "aeiou" and word[-1].lower() not in "aeiou" and word[-1].isalpha():
            # Check if word is longer than current longest word
            if longest_word is None or len(word) > len(longest_word):
                longest_word = word

    return longest_word