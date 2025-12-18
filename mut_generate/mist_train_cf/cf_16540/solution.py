"""
QUESTION:
Write a function `find_longest_word` that takes a list of words as input and returns the longest word that starts with a vowel and ends with a consonant. The function should have a time complexity of O(n), where n is the number of words in the input list. Each word in the list is guaranteed to be at least 8 characters long.
"""

def find_longest_word(dictionary):
    longest_word = ""
    for word in dictionary:
        if len(word) >= 8 and word[0] in "aeiou" and word[-1] not in "aeiou":
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word