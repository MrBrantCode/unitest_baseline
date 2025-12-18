"""
QUESTION:
Write a function named `same_letter_check` that takes a string `input_str` as input. The function should return a tuple containing a boolean value and an integer count. The boolean value indicates whether every word in `input_str` (excluding punctuation) begins and ends with the same letter, and the integer count is the number of words that meet this condition.
"""

import string

def same_letter_check(input_str):
    # Removing punctuation from the string
    my_string = "".join(char for char in input_str if char not in string.punctuation)
    words = my_string.split()   # Splitting string into words
    count = 0
    for word in words:
        if word[0].lower() == word[-1].lower():  # Comparing first and last characters of each word
            count += 1
    return (count == len(words), count)  # Returning boolean and count