"""
QUESTION:
Implement a function called getUniqueWords that takes a string of words as input, removes duplicates, and returns the unique words in reverse alphabetical order along with the total count of unique words. The function should not use built-in sorting functions or libraries, instead, it should implement its own sorting algorithm. The input string is in lowercase and words are separated by a space.
"""

def get_unique_words(input_string):
    """
    This function takes a string of words as input, removes duplicates, 
    and returns the unique words in reverse alphabetical order along 
    with the total count of unique words.

    Args:
        input_string (str): A string of words separated by a space.

    Returns:
        tuple: A tuple containing a list of unique words in reverse 
        alphabetical order and the total count of unique words.
    """

    # Split the input string into a list of words
    words = input_string.split()

    # Remove duplicates and store unique words
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    # Sort unique words in reverse alphabetical order using bubble sort
    for i in range(len(unique_words) - 1):
        for j in range(i + 1, len(unique_words)):
            if unique_words[i] < unique_words[j]:
                unique_words[i], unique_words[j] = unique_words[j], unique_words[i]

    # Return the unique words and their count
    return unique_words, len(unique_words)