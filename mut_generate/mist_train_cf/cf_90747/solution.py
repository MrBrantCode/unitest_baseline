"""
QUESTION:
Write a function `split_strings(lst, char)` that takes a list of strings `lst` and a character `char` as input. The function should split each string in `lst` into two substrings based on the first occurrence of `char`, and return a list of tuples containing the two substrings. If `char` does not appear in a string, the function should return ("None", "None") for that string. The function should also handle empty strings in `lst` by returning ("", "") for those strings.
"""

def entrance(lst, char):
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