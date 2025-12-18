"""
QUESTION:
Write a function `double_dict_values` that takes a dictionary `d` with integer values as input, creates a new dictionary where the values are doubled for every key, and handles potential exceptions that might arise during the computation. The function should exclude non-integer values from the new dictionary and return it. If an error occurs, the function should print an error message.
"""

def double_dict_values(d):
    try:
        return {k: v * 2 for k, v in d.items() if isinstance(v, int)}
    except Exception as e:
        print(f"An error occurred: {e}")