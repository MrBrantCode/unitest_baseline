"""
QUESTION:
Write a function named `count_unique_words` that takes a string `text` as input and returns the number of unique words in the text. The function should consider all words as case-insensitive, remove any leading or trailing spaces, and ignore punctuation marks and special characters. The time complexity should be O(n) and the space complexity should be O(n), where n is the number of characters in the text.
"""

def count_unique_words(text):
    # Convert the text to lowercase and remove leading/trailing spaces
    text = text.lower().strip()

    # Split the text into words using whitespace as the delimiter
    words = text.split()

    # Initialize an empty set to store unique words
    unique_words = set()

    # Iterate over each word and add it to the set
    for word in words:
        # Remove punctuation marks and special characters from the word
        word = ''.join(e for e in word if e.isalnum())
        # Add the word to the set
        unique_words.add(word)

    # Return the count of unique words
    return len(unique_words)