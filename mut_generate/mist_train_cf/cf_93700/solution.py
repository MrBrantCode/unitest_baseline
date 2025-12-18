"""
QUESTION:
Write a function named `split_strings` that takes a list of strings and a character as input. The function should split each string in the list into two substrings based on the first occurrence of the given character and return the substrings as a tuple. If the character is not found in a string, return `None` for that string. If a string is empty, return a tuple of two empty strings. The function should have a time complexity of O(n), where n is the total number of characters in all the input strings combined, and a space complexity of O(m), where m is the total number of input strings.
"""

def split_strings(strings, char):
    output = []
    for string in strings:
        if string == "":
            output.append(("", ""))
        elif char in string:
            index = string.index(char)
            output.append((string[:index], string[index+1:]))
        else:
            output.append(None)
    return output