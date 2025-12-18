"""
QUESTION:
Create a function named `count_letter_occurrences` that takes a string and a letter as input, and returns the number of occurrences of the letter in the string, considering both uppercase and lowercase letters, as well as letter accents. The function should be case-insensitive and accent-sensitive.
"""

def count_letter_occurrences(string, letter):
    count = 0
    for char in string:
        if char.lower() == letter.lower():
            count += 1
    return count