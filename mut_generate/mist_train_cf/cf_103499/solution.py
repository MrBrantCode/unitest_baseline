"""
QUESTION:
Create a function called `create_array` that takes two parameters, `num` and `string`. The function should return a list containing `num` and `string`. However, it should first check if `string` is a valid string consisting only of alphabetical characters. If `string` is invalid or contains non-alphabetical characters, the function should return an empty list.
"""

def create_array(num, string):
    if not isinstance(string, str) or not string.isalpha():
        return []
    return [num, string]