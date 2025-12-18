"""
QUESTION:
Write a function called `largest_alpha_subset` that takes a string as input and returns the length of the longest contiguous subset of alphabetic characters within the string.
"""

def largest_alpha_subset(text):
    largest = 0
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
            if count > largest:
                largest = count
        else:
            count = 0
    return largest