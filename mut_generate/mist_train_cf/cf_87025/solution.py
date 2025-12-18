"""
QUESTION:
Write a function called `find_longest_word` that takes a list of words as input and returns the longest word that starts with a vowel and ends with a consonant, given that each word is at least 8 characters long. The function should have a time complexity of O(n), where n is the number of words in the input list, and should not use any built-in Python functions or libraries for string manipulation or regular expressions.
"""

def find_longest_word(dictionary):
    longest_word = ""
    
    for word in dictionary:
        if len(word) >= 8 and word[0] in 'aeiou' and word[-1] not in 'aeiou':
            if len(word) > len(longest_word):
                longest_word = word
    
    return longest_word