"""
QUESTION:
Write a function called `most_frequent_letter` that takes a string of lowercase letters (with a maximum length of 100 characters) and returns the letter that appears most frequently. If multiple letters have the same maximum frequency, return the one that occurs first in the string.
"""

def most_frequent_letter(string):
    letter_count = {}
    max_count = 0
    most_frequent_letter = ""
    
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
        
        if letter_count[letter] > max_count:
            max_count = letter_count[letter]
            most_frequent_letter = letter
    
    return most_frequent_letter