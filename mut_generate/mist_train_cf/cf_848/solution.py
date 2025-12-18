"""
QUESTION:
Write a function named `calculate_unicode_sum` that takes a string as input. The function should return the sum of the Unicode values of all unique letters (a-z and A-Z) in the string, subtracting the Unicode values of special characters and ignoring duplicate letters.
"""

def calculate_unicode_sum(s):
    unicode_sum = 0
    visited_letters = set()

    for char in s:
        unicode_value = ord(char)

        if char.isalpha():
            if char.lower() not in visited_letters:
                visited_letters.add(char.lower())
                unicode_sum += unicode_value
        else:
            unicode_sum -= unicode_value

    return unicode_sum