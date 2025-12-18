"""
QUESTION:
Create a function named `count_letter_occurrences` that takes two parameters, a string and a letter. The function should return the number of occurrences of the given letter in the string, considering both uppercase and lowercase letters, as well as letter accents. The function should be case-insensitive.
"""

def count_letter_occurrences(string, letter):
    count = 0
    for char in string:
        if char.lower() == letter.lower():
            count += 1
    return count