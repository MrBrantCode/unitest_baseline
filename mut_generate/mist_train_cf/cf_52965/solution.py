"""
QUESTION:
Create a function named `prevalence_ratio` that takes in two parameters: `lexeme` (a string) and `strings` (a list of strings). The function should calculate and return the prevalence ratio of the `lexeme` within the `strings`, defined as the total count of occurrences of `lexeme` divided by the total count of words in the `strings`. The function should handle division by zero by returning 0 if the total count of words is zero.
"""

def prevalence_ratio(lexeme, strings):
    """
    This function returns the prevalence ratio of a particular lexeme 
    within an assortment of string constants.

    Args:
    lexeme (str): The target lexeme to find
    strings (list): The string assortment to search through

    Returns:
    float: The prevalence ratio of the lexeme in the strings 
    """

    # count the total number of occurrences of the lexeme
    count = sum(s.count(lexeme) for s in strings)

    # calculate the total number of words in the strings
    total = sum(len(s.split()) for s in strings)

    # calculate the prevalence ratio
    ratio = count / total if total != 0 else 0

    return ratio