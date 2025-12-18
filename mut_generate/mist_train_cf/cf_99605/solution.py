"""
QUESTION:
Create a function `check_sum(s)` that takes a string `s` as input, calculates the sum of the Unicode values of each character in the string, and returns "even" if the sum is even or "odd" if the sum is odd. The input string `s` will be a concatenation of all unique three-letter words that can be formed from the characters "dgikmqsuwy", where each character in the word must be adjacent to the next character in the string. The three-letter words are sorted in alphabetical order before concatenation.
"""

def entrance(s):
    total = sum(ord(char) for char in s)
    if total % 2 == 0:
        return "even"
    else:
        return "odd"