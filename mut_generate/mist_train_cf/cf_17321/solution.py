"""
QUESTION:
Create a function called `find_most_common_char` that takes a string as input. The string contains only alphabetic characters and spaces, may have leading or trailing spaces, and may be empty. The function should print out the most commonly-used character(s) in the string in alphabetical order. If there are multiple characters used the same number of times, print all of them. If the string is empty, print "No characters found."
"""

def find_most_common_char(string):
    string = string.strip().lower()
    char_freq = {}

    for char in string:
        if char != ' ':
            char_freq[char] = char_freq.get(char, 0) + 1

    if not char_freq:
        print("No characters found.")
        return

    max_freq = max(char_freq.values())
    most_common_chars = [char for char, freq in char_freq.items() if freq == max_freq]
    most_common_chars.sort()

    print("Most commonly-used character(s):", ", ".join(most_common_chars))