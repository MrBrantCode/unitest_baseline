"""
QUESTION:
Create a function `replace_string` that takes three parameters `string1`, `string2`, and `string3`, all consisting of only lowercase letters. The function should replace all instances of `string1` with `string2` in `string3` if `string1` is surrounded by spaces or at the beginning or end of `string3`. Return the modified `string3`.
"""

def replace_string(string1, string2, string3):
    """
    Replaces all instances of string1 with string2 in string3 if string1 is 
    surrounded by spaces or at the beginning or end of string3.

    Args:
        string1 (str): The string to be replaced.
        string2 (str): The string to replace with.
        string3 (str): The string in which replacement will occur.

    Returns:
        str: The modified string3 with replacements.
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