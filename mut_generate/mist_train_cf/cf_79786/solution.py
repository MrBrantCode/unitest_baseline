"""
QUESTION:
Write a function `transform_to_title_case` that takes a string of lowercase alphabets as input and returns the string in title case, where the first letter of each word is capitalized. The function should not capitalize letters after special characters or punctuation.
"""

def transform_to_title_case(input_str):
    return " ".join(word[0].upper() + word[1:] for word in input_str.split())