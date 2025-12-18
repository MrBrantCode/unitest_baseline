"""
QUESTION:
Create a function named `count_occurrences` that takes a string of text as input and returns a dictionary containing the number of occurrences of each alphanumeric character (letters and digits) and whitespace characters. The output dictionary should be sorted in ascending order of the characters' ASCII values.
"""

def count_occurrences(text):
    occurrences = {}
    for char in text:
        if char.isalnum() or char.isspace():
            if char in occurrences:
                occurrences[char] += 1
            else:
                occurrences[char] = 1
    return {k: v for k, v in sorted(occurrences.items(), key=lambda item: ord(item[0]))}