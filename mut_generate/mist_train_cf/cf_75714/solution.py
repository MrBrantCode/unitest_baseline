"""
QUESTION:
Create a function named `create_new_dict` that takes a dictionary as input, creates a new dictionary with the same keys, and assigns each key a value that is double its corresponding value in the original dictionary. The function must handle potential exceptions, such as non-numeric values, and return the new dictionary. The original dictionary may contain keys with numeric and non-numeric values.
"""

def create_new_dict(original_dict):
    new_dict = {}
    for key, value in original_dict.items():
        try:
            new_dict[key] = value * 2
        except TypeError:
            print(f"The value of key {key} cannot be doubled. It's not a number.")
    return new_dict