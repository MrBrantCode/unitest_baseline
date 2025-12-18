"""
QUESTION:
Create a function named `count_lowercase_letters` that takes a string as an input parameter and returns the total number of lowercase letters in the string. The string can contain special characters and numbers, which should be ignored in the count.
"""

def count_lowercase_letters(string):
    count = 0
    for ch in string:
        if ch.islower():
            count += 1
    return count