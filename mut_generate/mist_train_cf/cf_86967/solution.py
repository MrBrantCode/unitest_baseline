"""
QUESTION:
Write a function called `process_strings` that takes a list of strings as input. The function should remove any strings that contain special characters or numbers, convert all remaining strings to lowercase, remove duplicates, sort the remaining strings in alphabetical order, and count the occurrences of each string. The function should then return a dictionary where the keys are the unique strings and the values are their corresponding counts. The function should not take any other input and should not have any side effects other than returning the result.
"""

import re

def process_strings(strings):
    """
    Process a list of strings by removing special characters and numbers, 
    converting to lowercase, removing duplicates, sorting alphabetically, 
    and counting occurrences.

    Args:
        strings (list): A list of strings.

    Returns:
        dict: A dictionary with unique strings as keys and their counts as values.
    """
    # Convert strings to lowercase and remove special characters and numbers
    strings = [re.sub(r'[^a-zA-Z\s]', '', string.lower()) for string in strings]

    # Remove duplicates and sort strings alphabetically
    unique_strings = sorted(set(strings))

    # Count the occurrences of each string
    counts = {string: strings.count(string) for string in unique_strings}

    return counts