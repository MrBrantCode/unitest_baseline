"""
QUESTION:
Write a function `is_happy(s)` that takes a string `s` as input and returns `True` if the string is happy and `False` otherwise. A string is happy if it meets the following conditions:
- Its length is at least 3.
- Every 3 consecutive letters are distinct.
- Every distinct letter appears at least twice.
- There are no consecutive repeating letters.
- The sum of the occurrences of each distinct letter is an even number.
Use a dictionary to count the occurrences of each distinct letter.
"""

def is_happy(s):
    """
    Checks if a given string is happy.

    A string is happy if:
    - Its length is at least 3.
    - Every 3 consecutive letters are distinct.
    - Every distinct letter appears at least twice.
    - There are no consecutive repeating letters.
    - The sum of the occurrences of each distinct letter is an even number.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is happy, False otherwise.
    """

    # Check if string length is at least 3
    if len(s) < 3:
        return False

    # Check if any consecutive repeating letters
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False

    # Check if every 3 consecutive letters are distinct
    for i in range(len(s)-2):
        if len(set(s[i:i+3])) != 3:
            return False

    # Count the occurrences of each distinct letter
    letter_count = {}
    for letter in s:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # Check if every distinct letter appears at least twice and has an even count
    for count in letter_count.values():
        if count < 2 or count % 2 != 0:
            return False

    return True