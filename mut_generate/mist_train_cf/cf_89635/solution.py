"""
QUESTION:
Create a function named `count_uppercase_letters` that takes a string `text` as input. The function should return a dictionary where the keys are the uppercase letters in the string and the values are the corresponding counts of each uppercase letter, sorted in descending order of frequency.
"""

def count_uppercase_letters(text):
    uppercase_counts = {}
    for char in text:
        if char.isupper():
            uppercase_counts[char] = uppercase_counts.get(char, 0) + 1

    return dict(sorted(uppercase_counts.items(), key=lambda item: item[1], reverse=True))