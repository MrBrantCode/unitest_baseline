"""
QUESTION:
Write a function `find_longest_word(word_list)` that takes a list of words as input and returns the longest word that starts with a vowel and ends with a consonant, and contains at least two syllables. The function should ignore any words that contain numbers, special characters, or repeating letters. If no such word exists, the function should return `None`.
"""

def find_longest_word(word_list):
    vowels = 'aeiou'
    def count_syllables(word):
        count = 0
        for i in range(len(word)):
            if word[i].lower() in vowels and (i == 0 or word[i-1].lower() not in vowels):
                count += 1
        return count

    def is_valid(word):
        if any(char.isdigit() for char in word):
            return False
        if any(char.isalnum() for char in word) and len(set(word)) != len(word):
            return False
        return True

    longest_word = None
    for word in word_list:
        if word[0].lower() in vowels and word[-1].lower() not in vowels and count_syllables(word) >= 2 and is_valid(word):
            if longest_word is None or len(word) > len(longest_word):
                longest_word = word
    return longest_word