"""
QUESTION:
Create a function named `count_letters` that takes a string as input and returns a dictionary containing the count of each lowercase letter in the string. The function should exclude whitespace characters, punctuation marks, and numbers from being counted. The time complexity of the solution should be O(n) and the space complexity should be O(1), where n is the length of the string.
"""

def count_letters(string):
    letter_count = {}
    for char in string:
        if char.isalpha() and char.islower():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count