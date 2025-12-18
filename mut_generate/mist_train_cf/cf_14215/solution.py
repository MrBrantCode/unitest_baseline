"""
QUESTION:
Create a function named `create_dict` that takes a list of strings as input. The function should return a dictionary where each key is an odd index from the list and its corresponding value is the uppercase string from the list at that index, but only if the string is a vowel. The function should ignore non-vowel strings and strings at even indices.
"""

vowels = ["a", "e", "i", "o", "u"]

def create_dict(list):
    return {index: value.upper() for index, value in enumerate(list) if index % 2 != 0 and value.lower() in vowels}