"""
QUESTION:
Create a function named `count_uppercase_letters` that takes a string as input and returns a dictionary. The dictionary should contain the frequency of each uppercase letter in the input string, sorted in descending order of frequency.
"""

def count_uppercase_letters(text):
    uppercase_counts = {}
    for char in text:
        if char.isupper():
            uppercase_counts[char] = uppercase_counts.get(char, 0) + 1

    sorted_counts = dict(sorted(uppercase_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_counts