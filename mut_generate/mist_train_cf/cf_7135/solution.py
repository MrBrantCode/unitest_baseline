"""
QUESTION:
Write a function called `most_frequent_letter` that takes a string `s` as input, where `s` only contains lowercase letters and has a maximum length of 100 characters. The function should return the most frequently occurring letter in `s`. If multiple letters have the same maximum frequency, return the letter that appears first in the string. The function must have a time complexity of O(n), where n is the length of the string.
"""

def most_frequent_letter(s):
    count = {}
    max_count = 0
    most_frequent = ''
    for letter in s:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
        if count[letter] > max_count:
            max_count = count[letter]
            most_frequent = letter
    return most_frequent