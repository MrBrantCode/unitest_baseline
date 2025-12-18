"""
QUESTION:
Create a function `separate_numbers_letters` that takes a list of alphanumeric strings as input. The function should return a new list where each entry is an object containing two properties: `numbers` — an array of the numbers from the string in order of occurrence, and `letters` — a hash map in which the key is the letter from the string and the value is the number of occurrences. The function should work for an input list of arbitrary length and have a computational complexity that can handle the worst-case scenario where all strings in the input list have the same large length n.
"""

import re

def separate_numbers_letters(lst):
    output = []
    for string in lst:
        obj = {'numbers': [], 'letters': {}}
        obj['numbers'] = [int(num) for num in re.findall('\d+', string)]
        for char in re.findall('[a-zA-Z]', string):
            if char in obj['letters']:
                obj['letters'][char] += 1
            else:
                obj['letters'][char] = 1
        output.append(obj)
    return output