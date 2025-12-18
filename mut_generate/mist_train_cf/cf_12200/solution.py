"""
QUESTION:
Write a function called `string_formatter` that takes a string as input, splits it into a list of words, removes any duplicate words, and returns the list of unique words in alphabetical order. The input string may contain lowercase and uppercase letters, numbers, spaces, and punctuation marks. Do not use any built-in functions or libraries that directly solve this problem.
"""

def string_formatter(input_string):
    """
    This function takes a string as input, splits it into a list of words, removes any duplicate words, 
    and returns the list of unique words in alphabetical order.

    Args:
        input_string (str): The input string that needs to be formatted.

    Returns:
        list: A list of unique words in alphabetical order.
    """

    # Split the string into a list of words
    word_list = input_string.split()

    # Initialize an empty dictionary to store unique words
    unique_words = {}

    # Iterate over each word in the list
    for word in word_list:
        # Remove leading and trailing punctuation marks
        clean_word = ''
        for char in word:
            if char.isalnum():
                clean_word += char

        # Convert the word to lowercase
        clean_word = clean_word.lower()

        # Add the word to the dictionary
        unique_words[clean_word] = True

    # Convert the dictionary keys to a list and sort them
    sorted_words = sorted(unique_words.keys())

    return sorted_words