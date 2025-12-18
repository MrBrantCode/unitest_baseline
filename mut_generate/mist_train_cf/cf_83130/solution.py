"""
QUESTION:
Write a function called `modify_string` that takes a string as input, replaces all exclamation marks with periods, and returns the modified string. The function should also handle potential exceptions.
"""

def modify_string(s):
    try:
        return s.replace("!", ".")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None