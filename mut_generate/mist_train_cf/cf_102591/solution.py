"""
QUESTION:
Create a function called `convert_to_unique_list` that takes a string of space-separated words as input and returns a list of unique words. The order of the words in the resulting list should be the same as their order in the original string.
"""

def convert_to_unique_list(input_string):
    """
    This function takes a string of space-separated words as input and returns a list of unique words.
    The order of the words in the resulting list is the same as their order in the original string.

    Args:
        input_string (str): A string of space-separated words.

    Returns:
        list: A list of unique words.
    """
    word_list = input_string.split(" ")
    unique_word_set = set()
    unique_word_list = []
    
    for word in word_list:
        if word not in unique_word_set:
            unique_word_set.add(word)
            unique_word_list.append(word)
            
    return unique_word_list