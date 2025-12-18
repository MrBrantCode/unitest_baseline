"""
QUESTION:
Create a function named `find_most_common_character` that takes a string as input. The function should convert the string to lowercase, ignore leading/trailing spaces, and print out the most frequently occurring character(s) in alphabetical order. If there are multiple characters with the same highest frequency, print all of them. If the string is empty, print "No characters found." The function should be able to handle strings of up to 10^6 characters efficiently.
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