"""
QUESTION:
Create a function named `count_char` that takes a string `text` as input. The function should construct a dictionary that records the unique alphanumeric characters in the string and their respective occurrence counts. The function should be case-insensitive and ignore non-alphanumeric characters, including punctuation and whitespaces. The function should return or print the dictionary.
"""

import string

def count_char(text):
    count_dict = {}
    for char in text.lower():
        if char in string.ascii_lowercase or char.isdigit():  
            if char in count_dict:
                count_dict[char] += 1  
            else:
                count_dict[char] = 1  
    return count_dict