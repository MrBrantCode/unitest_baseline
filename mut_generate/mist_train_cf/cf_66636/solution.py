"""
QUESTION:
Write a function called `find_recurring_char` that takes a string `text` as input and returns the first recurring alphabetic character along with the index positions of its first and second occurrence. The function should be case-insensitive and ignore non-alphabetic characters. If no recurring character is found, it should return the message "No recurring character found in given text."
"""

def find_recurring_char(text):
    char_dict = {}
    for i, char in enumerate(text):
        if not char.isalpha():
            continue

        char = char.lower()

        if char in char_dict:
            return (char, char_dict[char], i)

        char_dict[char] = i

    return "No recurring character found in given text."