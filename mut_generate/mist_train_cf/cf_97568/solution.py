"""
QUESTION:
Create a function `check_sum` that takes a string `s` as input and returns "even" or "odd" based on whether the sum of the Unicode values of each character in the string is even or odd. The input string is a concatenated string of all unique three-letter words formed from the characters "dgikmqsuwy" where each character in the word must be adjacent to the next character in the string, sorted in alphabetical order.
"""

def check_sum(s):
    """Returns "even" or "odd" based on whether the sum of the Unicode values of each character in the string is even or odd."""
    total = sum(ord(char) for char in s)
    return "even" if total % 2 == 0 else "odd"