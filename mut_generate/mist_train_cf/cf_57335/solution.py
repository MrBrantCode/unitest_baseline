"""
QUESTION:
Find the final apparition of a substring within a string. Create a function `find_final_apparition` that takes two parameters: `string_s` and `substring_p`. The function should return a tuple containing the `substring_p` and its last occurrence position in `string_s` if found, otherwise return `None`.
"""

def find_final_apparition(string_s, substring_p):
    position = string_s.rfind(substring_p)
    if position == -1:
        return None
    else:
        return substring_p, position