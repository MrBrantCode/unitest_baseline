"""
QUESTION:
Write a function `split_strings` that takes a list of strings and a character as input. The function should return a list of tuples, where each tuple contains two substrings split from the corresponding input string based on the first occurrence of the character. If the character is not found in a string, return `None` for that string. If the input string is empty, return `("", "")`. The time complexity should be O(n) and the space complexity should be O(m), where n is the total number of characters in all the input strings combined, and m is the total number of input strings.
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