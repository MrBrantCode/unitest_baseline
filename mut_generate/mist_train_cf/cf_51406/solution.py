"""
QUESTION:
Create a function `char_counts` that takes a string as input and returns a dictionary where the keys are the unique alphabetical characters from the input string (in lowercase) and the values are their respective frequencies.
"""

def char_counts(text):
    counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts