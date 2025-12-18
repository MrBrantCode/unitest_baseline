"""
QUESTION:
Write a function `retrieve_tuples` that takes a string of a list of tuples in the format "[('name1', age1), ('name2', age2), ...]" and returns a list of tuples with names that start with a consonant, sorted by the length of the name in descending order. The function should extract the names and ages from the string, filter out tuples with names starting with a vowel, and then sort the remaining tuples based on the length of the name.
"""

import re

def retrieve_tuples(string):
    pattern = r"\('([a-zA-Z]+)', (\d+)\)"
    matches = re.findall(pattern, string)
    filtered_tuples = [(name, age) for name, age in matches if name[0].lower() not in 'aeiou']
    sorted_tuples = sorted(filtered_tuples, key=lambda x: len(x[0]), reverse=True)
    return sorted_tuples