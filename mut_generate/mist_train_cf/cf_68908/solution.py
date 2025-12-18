"""
QUESTION:
Write a function named `reverse_string_words` that takes two parameters: `s` (a string containing words separated by commas, spaces, or both) and `target` (a word to be excluded from the result). The function should return a list of words from the input string, excluding the target word, in reverse order.
"""

def reverse_string_words(s, target):
    replaced = s.replace(",", " ").replace(".", " ")
    split_words = replaced.split()
    split_words = [word for word in split_words if word != target]
    return split_words[::-1]