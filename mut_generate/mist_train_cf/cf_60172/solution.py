"""
QUESTION:
Write a function `transform_sequence(s, target)` that takes a string `s` and a target word `target` as input, splits the string into a list of words while maintaining the original sequence, ignores the target word if it appears, and handles erroneous inputs with special characters. The function should return the list of words with the target word removed.
"""

def transform_sequence(s, target):
    s_list = s.replace(',', '').split()
    s_list = [word for word in s_list if word != target]
    return s_list