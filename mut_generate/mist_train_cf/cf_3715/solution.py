"""
QUESTION:
Design a function `longest_word` that takes an array of strings as input, where each string can contain special characters and whitespace. The function should return the longest word from the array without using any built-in functions or libraries to find the longest word. If multiple words have the same maximum length, the function should return the word that appears first in the array. If the array is empty or contains only empty strings, the function should return an empty string. The time complexity of the function should be O(n), where n is the total number of characters in all the strings combined.
"""

def longest_word(arr):
    maxWord = ""
    maxLen = 0
    for str in arr:
        word = ""
        len_ = 0
        for c in str:
            if not c.isalnum():
                if len_ > maxLen:
                    maxLen = len_
                    maxWord = word
                word = ""
                len_ = 0
            else:
                word += c
                len_ += 1
        if len_ > maxLen:
            maxLen = len_
            maxWord = word
    return maxWord