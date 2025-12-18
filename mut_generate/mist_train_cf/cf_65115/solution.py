"""
QUESTION:
Write a function `reverseWords(s)` that takes an input string `s` containing English letters (upper-case and lower-case), digits, and spaces, and returns a string where each word is reversed, but the sequence of words remains the same, joined by a single space. The input string may contain spaces at the beginning or end, or multiple spaces between two words, but the output string should not have any leading or trailing spaces. The length of the input string is between 1 and 10^4, and it contains at least one word.
"""

def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)