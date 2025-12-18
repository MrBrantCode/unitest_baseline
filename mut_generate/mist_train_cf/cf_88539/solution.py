"""
QUESTION:
Write a function named `count_occurrences` that takes two arguments: a string and a character. The function should count the number of occurrences of the character in the string, ignoring any occurrences that are preceded or followed by the same character, or are within parentheses, square brackets, single quotes, or double quotes. The function is case-sensitive and considers special characters and numbers in the string.
"""

def count_occurrences(string, character):
    count = 0
    in_quotes = False
    in_parentheses = False
    in_square_brackets = False

    for i in range(len(string)):
        if string[i] == character:
            if in_quotes or in_parentheses or in_square_brackets:
                continue
            if i > 0 and string[i-1] == character:
                continue
            if i < len(string)-1 and string[i+1] == character:
                continue
            count += 1

        if string[i] == "'" or string[i] == '"':
            if in_quotes and string[i-1] != "\\":
                in_quotes = False
            elif not in_quotes:
                in_quotes = True
        elif string[i] == "(":
            in_parentheses = True
        elif string[i] == ")":
            in_parentheses = False
        elif string[i] == "[":
            in_square_brackets = True
        elif string[i] == "]":
            in_square_brackets = False

    return count