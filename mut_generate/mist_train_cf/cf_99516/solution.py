"""
QUESTION:
Write a function `find_longest_word` that takes a string `paragraph` as input, splits it into words and returns the longest word. The function should be able to handle multiple paragraphs in a text file. The input string may contain multiple words of different lengths separated by spaces.
"""

def find_longest_word(paragraph):
    words = paragraph.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word