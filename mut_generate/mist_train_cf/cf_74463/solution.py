"""
QUESTION:
Write a function `is_isomorphic(word1, word2)` that determines if two input strings are isomorphic without using any built-in functions. Two strings are isomorphic if the characters in one string can be replaced to get the other string, where each character can be replaced by only one unique character. The function should return True if the strings are isomorphic and False otherwise.
"""

def is_isomorphic(word1, word2):
    # Check if words are same length
    if len(word1) != len(word2):
        return False

    # Initialize two dictionaries
    dict1 = {}
    dict2 = {}

    # Loop through each character in the words
    for i in range(len(word1)):
        letter1 = word1[i]
        letter2 = word2[i]

        # If the letters are not in their respective dictionary, add them
        if letter1 not in dict1:
            dict1[letter1] = letter2

        if letter2 not in dict2:
            dict2[letter2] = letter1

        # If the letters do not match up with the previously matched pairs, return False
        if dict1[letter1] != letter2 or dict2[letter2] != letter1:
            return False

    # If all letters match up, the words are isomorphic
    return True