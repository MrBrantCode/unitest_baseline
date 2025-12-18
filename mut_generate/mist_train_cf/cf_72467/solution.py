"""
QUESTION:
Create a function `longest_word_and_length` that takes a string value, finds the longest word in that string, and returns both the word and its length as a tuple. The input string should be split into words by spaces. The function should handle sentences with multiple words of the same maximum length by returning any of the longest words.
"""

def longest_word_and_length(sentence):
    words = sentence.split(" ")
    longest = max(words, key=len)
    return longest, len(longest)