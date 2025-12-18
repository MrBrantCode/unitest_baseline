"""
QUESTION:
Write a function `transform_sequence` that takes a string `sequence` and a boolean `is_punct_to_asterisk` as inputs. The function should replace all punctuation symbols in the string with asterisks if `is_punct_to_asterisk` is `True`, and replace all asterisks with their corresponding punctuation symbols if `is_punct_to_asterisk` is `False`. Use a dictionary to map punctuation symbols to asterisks and vice versa.
"""

import string

def transform_sequence(sequence, is_punct_to_asterisk):
    transformation_dict = {symbol: "*" for symbol in string.punctuation}
    reverse_transformation_dict = {y: x for x, y in transformation_dict.items()}

    for k,v in (transformation_dict if is_punct_to_asterisk else reverse_transformation_dict).items():
        sequence = sequence.replace(k,v)
    return sequence