"""
QUESTION:
Write a function `compute_occurrences` that takes a string as input and returns a dictionary where the keys are the characters in the string and the values are the occurrences of each character. The function should count all characters, including spaces and punctuation.
"""

def compute_occurrences(my_string):
    count_dict = {}
    for c in my_string:
        count_dict[c] = count_dict.get(c, 0) + 1
    return count_dict