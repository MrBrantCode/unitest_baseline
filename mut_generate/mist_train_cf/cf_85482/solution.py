"""
QUESTION:
Create a function `sort_dict` that takes a dictionary as an argument. The function should reorder the dictionary based on the numerical values in descending order. If there are ties in the numerical values, the keys should be sorted alphabetically in ascending order. The function should return the reordered dictionary.
"""

def sort_dict(my_dict):
    sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: (-item[1], item[0]))}
    return sorted_dict