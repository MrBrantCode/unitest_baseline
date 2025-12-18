"""
QUESTION:
Create a function `replace_string` that takes three parameters: `string1`, `string2`, and `string3`. Replace all instances of `string1` with `string2` in `string3` only if `string1` is surrounded by spaces or at the beginning or end of `string3`. The function should return the modified `string3`. The function should assume that all strings will consist of only lowercase letters.
"""

def replace_string(string1, string2, string3):
    """
    Replace all instances of `string1` with `string2` in `string3` only if `string1` is surrounded by spaces or at the beginning or end of `string3`.

    Args:
        string1 (str): The string to be replaced.
        string2 (str): The replacement string.
        string3 (str): The original string.

    Returns:
        str: The modified `string3` with all instances of `string1` replaced with `string2` if the condition is met.
    """
    result = ""
    index = 0

    while index < len(string3):
        if string3[index:index+len(string1)] == string1:
            if (index == 0 or string3[index-1] == " ") and (index + len(string1) == len(string3) or string3[index+len(string1)] == " "):
                result += string2
                index += len(string1)
                continue
        
        result += string3[index]
        index += 1

    return result