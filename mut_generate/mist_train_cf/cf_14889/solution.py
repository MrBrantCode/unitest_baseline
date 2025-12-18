"""
QUESTION:
Create a function `count_occurrences` that takes a string of printable ASCII characters as input and returns a dictionary containing the number of occurrences of each alphanumeric character and whitespace. The dictionary should be sorted in ascending order of the characters' ASCII values. Non-alphanumeric characters other than whitespace should not be counted.
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