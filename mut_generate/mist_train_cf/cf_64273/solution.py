"""
QUESTION:
Write a function `invert_word_sequence(s)` that takes a string `s` as input and returns a string with the words in inverted order, joined by a single space. The input string may contain spaces at the beginning or end, or multiple spaces between words. The output string should not have any additional spaces. The input string will contain at least one word and consist of English letters (both uppercase and lowercase), digits, and spaces, with a length between 1 and 104.
"""

def invert_word_sequence(s):
    # split the string into list of words
    s = s.split()
    
    # reverse the list
    s = s[::-1]
    
    # join the list to form a string with space separated words
    return ' '.join(s)