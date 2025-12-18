"""
QUESTION:
Write a function `check_sum` that takes a string `long_string` as input, calculates the sum of the Unicode values of each character, and returns "even" if the sum is even and "odd" if the sum is odd. The input string `long_string` will be a concatenated string of all possible three-letter words that can be formed from the string "dgikmqsuwy" with each character adjacent to the next character in the string, sorted in alphabetical order.
"""

def check_sum(long_string):
    total = sum(ord(char) for char in long_string)
    if total % 2 == 0:
        return "even"
    else:
        return "odd"