"""
QUESTION:
Write a function `alphabetize_and_count(s)` that takes a string `s` as input and returns a tuple containing the string with its characters in alphabetical order and a dictionary where each key is a unique character from the string and its corresponding value is the frequency of that character.
"""

def alphabetize_and_count(s):
    sorted_string = "".join(sorted(s))
    freq = {}
    for char in sorted_string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return sorted_string, freq