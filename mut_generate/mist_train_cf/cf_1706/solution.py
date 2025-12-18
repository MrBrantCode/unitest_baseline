"""
QUESTION:
Create a function called `count_unique_chars` that takes a string `s` as input. The function should return a tuple containing the length of the string (ignoring whitespace characters), the number of unique characters in the string (ignoring whitespace characters), the number of special characters or digits in the string, and the number of consecutive uppercase letters in the string.
"""

def count_unique_chars(s):
    unique_chars = set()
    consecutive_uppercase_count = 0
    special_char_digit_count = 0

    # Remove whitespace characters from the string
    s = ''.join(s.split())

    for i in range(len(s)):
        # Count unique characters
        unique_chars.add(s[i])

        # Check for consecutive uppercase letters
        if i > 0 and s[i].isupper() and s[i-1].isupper():
            consecutive_uppercase_count += 1

        # Check for special characters or digits
        if not s[i].isalpha():
            special_char_digit_count += 1

    return len(s), len(unique_chars), special_char_digit_count, consecutive_uppercase_count