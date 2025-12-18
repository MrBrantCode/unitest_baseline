"""
QUESTION:
Create a function `filter_tuples` that takes a string representing a list of tuples as input. The string will have the format: "[('name1', age1), ('name2', age2), ...]". Return a list of tuples from the input string, excluding tuples where the person's name starts with a vowel (a, e, i, o, u). The output should contain only tuples where the person's name starts with a consonant.
"""

import ast

def filter_tuples(string):
    # Convert the string to a list of tuples
    tuples = ast.literal_eval(string)
    
    # Filter out tuples where the person's name starts with a vowel
    filtered_tuples = [t for t in tuples if t[0][0].lower() not in ['a', 'e', 'i', 'o', 'u']]
    
    return filtered_tuples