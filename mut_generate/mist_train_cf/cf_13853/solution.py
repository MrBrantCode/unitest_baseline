"""
QUESTION:
Write a function named `most_frequent_letter` that takes a string of at most 100 lowercase characters and returns the letter that appears most frequently.
"""

def most_frequent_letter(string):
    letter_count = {}
    max_count = 0
    most_frequent_letter = ''

    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

        if letter_count[letter] > max_count:
            max_count = letter_count[letter]
            most_frequent_letter = letter

    return most_frequent_letter