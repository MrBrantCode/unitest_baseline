"""
QUESTION:
Write a function `word_count` that takes a string and a delimiter as input, splits the string into words using the delimiter, counts the occurrences of each word in a case-insensitive manner, and returns a dictionary where the keys are the words and the values are their corresponding counts. The function should ignore case differences when counting word occurrences.
"""

def word_count(string, delimiter):
    """
    This function takes a string and a delimiter as input, splits the string into words 
    using the delimiter, counts the occurrences of each word in a case-insensitive 
    manner, and returns a dictionary where the keys are the words and the values are 
    their corresponding counts.

    Args:
        string (str): The input string.
        delimiter (str): The delimiter used to split the string.

    Returns:
        dict: A dictionary where the keys are the words and the values are their 
        corresponding counts.
    """
    # Split the string by the specified delimiter and convert to lower case
    split_string = string.lower().split(delimiter)

    # Initialize an empty dictionary for word counts 
    word_counts = {}

    # Go through each word in the split string
    for word in split_string:
        # If the word is not in the dictionary yet, add it with a count of 1
        if word not in word_counts:
            word_counts[word] = 1
        # If the word is already in the dictionary, increment its count by 1
        else:
            word_counts[word] += 1

    return word_counts