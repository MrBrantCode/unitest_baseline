"""
QUESTION:
Write a function called `word_count` that takes a string of words as input and returns a dictionary where the keys are the unique words in the string and the values are their corresponding counts. The string may contain multiple words separated by spaces.
"""

def word_count(text):
    """
    This function takes a string of words as input and returns a dictionary 
    where the keys are the unique words in the string and the values are their corresponding counts.

    Parameters:
    text (str): The input string of words.

    Returns:
    dict: A dictionary where the keys are the unique words in the string and the values are their corresponding counts.
    """
    words = text.split()
    count = dict()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count