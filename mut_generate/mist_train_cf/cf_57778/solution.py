"""
QUESTION:
Write a function `sum_hours_by_word` that takes a 2D list `data` and a string `word` as input, where each inner list represents a row in a spreadsheet. The first element of each inner list is a word, and the second element is the corresponding hours. The function should return the sum of hours for rows where the word matches the input `word`.
"""

def sum_hours_by_word(data, word):
    """
    Returns the sum of hours for rows where the word matches the input word.

    Args:
        data (list): A 2D list where each inner list represents a row in a spreadsheet.
        word (str): The word to match in the spreadsheet.

    Returns:
        int: The sum of hours for rows where the word matches the input word.
    """
    return sum(hours for row_word, hours in data if row_word == word)