"""
QUESTION:
Implement a function `find_words_with_al` that takes a string `document` as input and returns a list of words that contain the substring "al" in a case-insensitive manner. The solution should not use any built-in string matching or substring searching functions or libraries, and it should have a time complexity of O(n * m), where n is the size of the document and m is the average number of characters per word in the document.
"""

def find_words_with_al(document):
    """
    This function finds and returns a list of words that contain the substring "al" in a case-insensitive manner.

    Args:
        document (str): The input string document.

    Returns:
        list: A list of words that contain the substring "al".
    """

    # Split the document into individual words
    words = document.split()

    # Initialize an empty list to store words that contain the substring "al"
    words_with_al = []

    # Iterate through each word in the document
    for word in words:
        # Convert the word to lowercase for case-insensitive matching
        word_lower = word.lower()
        
        # Check if the word contains the substring "al"
        for i in range(len(word_lower) - 1):
            # Check if the current character matches 'a' and the next character matches 'l'
            if word_lower[i] == 'a' and word_lower[i + 1] == 'l':
                # Add the word to the list if it contains the substring "al"
                words_with_al.append(word)
                break

    # Return the list of words that contain the substring "al"
    return words_with_al