"""
QUESTION:
Create a function named `count_occurrences` that takes an input string and a character as parameters. The function should count the occurrences of the given character in the input string, but only if the character is surrounded by a pair of non-nested parentheses. The function should return the count of such occurrences. The input string and character can contain any valid characters, and the input string can have any number of pairs of parentheses, but only count occurrences of the character that are directly surrounded by a pair of parentheses (i.e., not nested within another pair).
"""

def count_occurrences(input_string, character):
    """
    Counts the occurrences of a character in an input string, 
    but only if the character is surrounded by a pair of non-nested parentheses.

    Args:
        input_string (str): The input string to search for the character.
        character (str): The character to search for.

    Returns:
        int: The count of occurrences of the character surrounded by non-nested parentheses.
    """
    count = 0
    parentheses_count = 0

    for i in range(len(input_string)):
        if input_string[i] == '(':
            parentheses_count += 1
        elif input_string[i] == ')':
            parentheses_count -= 1

        if parentheses_count == 1 and input_string[i] == character:
            count += 1

    return count