"""
QUESTION:
Write a function named `invert_dict` that takes a dictionary `original_dict` as input and returns a new dictionary where each key-value pair is inverted, i.e., the original key becomes the value and the original value becomes the key. If the original dictionary contains duplicate values, the function should group the corresponding keys into a sorted list in the new dictionary.
"""

def invert_dict(original_dict):
    inverse_dict = {}
    for key, value in original_dict.items():
        if value not in inverse_dict:
            inverse_dict[value] = [key]
        else:
            inverse_dict[value].append(key)
            inverse_dict[value].sort()
    return inverse_dict