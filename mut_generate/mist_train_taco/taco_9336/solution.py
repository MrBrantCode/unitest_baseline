"""
QUESTION:
Write a function called "filterEvenLengthWords".

Given an array of strings, "filterEvenLengthWords" returns an array containing only the elements of the given array whose length is an even number.

var output = filterEvenLengthWords(['word', 'words', 'word', 'words']);

console.log(output); // --> ['word', 'word']
"""

def filter_even_length_words(words):
    """
    Filters the given list of strings to return only those whose length is an even number.

    Parameters:
    words (list of str): The list of strings to filter.

    Returns:
    list of str: A list containing only the strings from the input list whose length is even.
    """
    return [word for word in words if len(word) % 2 == 0]