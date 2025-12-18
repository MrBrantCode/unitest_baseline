"""
QUESTION:
Create a function named `split_strings` that takes a list of strings and a character as input. The function should split each string in the list into two substrings at the first occurrence of the given character, if present, and return the substrings as a tuple. If the character is not found in a string, return ("None", "None") for that string. If the input list contains an empty string, return ("", "") for that string.
"""

def split_strings(lst, char):
    result = []
    for string in lst:
        if not string:
            result.append(("", ""))
        elif char in string:
            index = string.index(char)
            substring1 = string[:index]
            substring2 = string[index+1:]
            result.append((substring1, substring2))
        else:
            result.append(("None", "None"))
    return result