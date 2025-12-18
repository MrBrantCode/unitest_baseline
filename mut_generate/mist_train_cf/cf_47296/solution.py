"""
QUESTION:
Write a function `sort_dict_by_value` that takes a dictionary as input and returns a dictionary sorted by its values. The function should maintain the original key-value structure and should not alter the keys. The function should be compatible with Python 3.7+ where the built-in dict maintains the insertion order. 

Restrictions: 
- The input dictionary is unordered.
- The function should return a dictionary, not a list of tuples or other data structures.
- The function should handle dictionaries with duplicate values by maintaining the original key-value structure.
- The function should be efficient and have minimal alterations to the keys.
"""

def sort_dict_by_value(input_dict):
    return dict(sorted(input_dict.items(), key=lambda item: item[1]))