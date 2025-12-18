"""
QUESTION:
Create a function called `find_most_common_character` that takes a string as input. The string may contain alphanumeric characters, spaces, and special characters. The function should convert the string to lowercase, handle strings with leading or trailing spaces, and print out the most commonly-used character(s) in alphabetical order. If the string is empty or contains only spaces, the function should print "No characters found." The function should be able to handle strings of length up to 10^6 characters efficiently.
"""

from collections import defaultdict

def find_most_common_character(string):
    string = string.strip().lower()

    if not string:
        print("No characters found.")
        return

    frequency = defaultdict(int)
    max_frequency = 0

    for char in string:
        frequency[char] += 1
        max_frequency = max(max_frequency, frequency[char])

    most_common_chars = [char for char, count in frequency.items() if count == max_frequency]
    most_common_chars.sort()

    print(''.join(most_common_chars))