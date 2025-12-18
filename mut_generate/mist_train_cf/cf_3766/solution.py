"""
QUESTION:
Create a function called `retrieve_tuples` that takes a string as input, where the string contains a list of tuples in the format "[('name1', age1), ('name2', age2), ...]". The function should extract the tuples from the string, filter out any tuples where the person's name starts with a vowel, and return the remaining tuples sorted in descending order based on the length of the person's name.
"""

import re

def retrieve_tuples(string):
    pattern = r"\('([a-zA-Z]+)', (\d+)\)"
    matches = re.findall(pattern, string)
    filtered_tuples = [(name, age) for name, age in matches if name[0].lower() not in 'aeiou']
    sorted_tuples = sorted(filtered_tuples, key=lambda x: len(x[0]), reverse=True)
    return sorted_tuples