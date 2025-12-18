"""
QUESTION:
Create a function named `count_letters` that takes a list of letters as input and returns a dictionary where the keys are the unique letters in the input list and the values are the counts of each letter. The function should iterate through the input list to count the occurrences of each letter.
"""

def count_letters(letter_list):
    """
    Counts the occurrences of each letter in a list and returns a dictionary where the keys are the unique letters and the values are the counts.
    
    Args:
        letter_list (list): A list of letters.
    
    Returns:
        dict: A dictionary with unique letters as keys and their counts as values.
    """
    letter_count = {}
    for letter in letter_list:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count