"""
QUESTION:
Write a function named `count_strings` that takes a list of strings as input. The function should count the occurrences of each string that contains the letter "a" and does not start with a capital letter. The function should return a dictionary where the keys are the strings containing "a" and the values are their respective counts.
"""

def count_strings(strings):
    counts = {}
    for string in strings:
        if string[0].isupper():
            continue
        if 'a' in string:
            counts[string] = counts.get(string, 0) + 1
    return counts