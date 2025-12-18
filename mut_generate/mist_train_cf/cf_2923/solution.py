"""
QUESTION:
Create a function called `count_occurrences` that takes two parameters: `string` and `substring`. Implement a case-sensitive search for all occurrences of `substring` within `string` without using built-in string methods or regular expressions. The function should return the total number of occurrences and the positions of the occurrences.
"""

def count_occurrences(string, substring):
    """
    Counts the occurrences of a substring in a string and returns the total count and positions.
    
    Parameters:
    string (str): The input string to search in.
    substring (str): The substring to search for.
    
    Returns:
    tuple: A tuple containing the total number of occurrences and a list of positions.
    """
    occurrences = 0
    positions = []

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            occurrences += 1
            positions.append(i)

    return occurrences, positions