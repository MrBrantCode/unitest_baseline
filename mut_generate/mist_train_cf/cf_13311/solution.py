"""
QUESTION:
Create a function named `replace_and_count` that takes a string and two words (a keyword and a replacement word) as input. The function should replace all occurrences of the keyword with the replacement word in the given string, ignoring occurrences where the keyword is part of another word. The function should be case-sensitive and return the modified string along with the total number of occurrences of the keyword in the string.
"""

def replace_and_count(string, keyword, replacement):
    """
    Replaces all occurrences of a keyword with a replacement word in a given string,
    ignoring occurrences where the keyword is part of another word.

    Args:
        string (str): The input string.
        keyword (str): The word to be replaced.
        replacement (str): The replacement word.

    Returns:
        tuple: A tuple containing the modified string and the total number of occurrences of the keyword.

    """
    count = 0
    words = string.split()
    for i in range(len(words)):
        if words[i] == keyword:
            words[i] = replacement
            count += 1
    new_string = ' '.join(words)
    return new_string, count