"""
QUESTION:
Write a function `filter_tuples` that takes a string as input, representing a list of tuples in the format "[('name1', age1), ('name2', age2), ...]". The function should convert the string into a list of tuples and then filter out any tuples where the person's name starts with a vowel. The function should return a list of tuples where the person's name starts with a consonant.
"""

import ast

def filter_tuples(string):
    # Convert the string to a list of tuples
    tuples = ast.literal_eval(string)
    
    # Filter out tuples where the person's name starts with a vowel
    filtered_tuples = [t for t in tuples if t[0][0].lower() not in ['a', 'e', 'i', 'o', 'u']]
    
    return filtered_tuples