"""
QUESTION:
Create a function called `advanced_histogram` that takes a string as input and returns a dictionary where the keys are the unique characters in the string (with uppercase and lowercase characters treated as equivalent) and numerical values and punctuation marks treated as distinct keys, and the values are the number of occurrences of each of these characters.
"""

def advanced_histogram(test):
    histogram_dict = {}
    for char in test:
        if char.isalpha():
            char = char.lower()
        if char in histogram_dict:
            histogram_dict[char] += 1
        else:
            histogram_dict[char] = 1
    return histogram_dict