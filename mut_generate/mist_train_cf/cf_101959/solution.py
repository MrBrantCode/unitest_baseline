"""
QUESTION:
Write a function `reverse_words` that takes a string of comma-separated words as input and returns a string with the words in reverse order. The input string contains at most 100 words, each with at most 50 characters, and the output should preserve the original capitalization of the words.
"""

def reverse_words(string):
    words = string.split(",")
    result = ""
    for word in reversed(words):
        result += word + ","
    result = result.rstrip(",")
    return result