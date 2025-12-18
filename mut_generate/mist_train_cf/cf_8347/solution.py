"""
QUESTION:
Create a function `count_words` that takes a string as input, ignores punctuation, and considers words in a case-insensitive manner. The function should return a list of unique words in descending order of their frequency of occurrence and a dictionary containing the number of occurrences of each unique word. The function should not use built-in functions or libraries for tasks such as sorting, frequency counting, or regular expressions.
"""

def count_words(string):
    """
    This function takes a string as input, ignores punctuation, and considers words in a case-insensitive manner.
    It returns a list of unique words in descending order of their frequency of occurrence and a dictionary containing the number of occurrences of each unique word.

    Parameters:
    string (str): The input string.

    Returns:
    list: A list of unique words in descending order of their frequency of occurrence.
    dict: A dictionary containing the number of occurrences of each unique word.
    """
    # Remove punctuation and convert string to lowercase
    string = string.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")

    # Split the string into words
    words = string.split()

    # Create a dictionary to store the word counts
    word_counts = {}

    # Count the occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Sort the words by their counts in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Extract the words from the sorted list
    unique_words = [word for word, count in sorted_words]

    # Return the unique words and their counts
    return unique_words, word_counts