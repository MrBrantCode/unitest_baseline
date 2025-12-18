"""
QUESTION:
Create a function `word_frequency` that takes a string of text as input. The function should ignore punctuation, treat uppercase and lowercase letters as equivalent, and handle large input strings efficiently. It should return a list of unique words along with their frequencies in descending order.
"""

def word_frequency(text):
    # Remove punctuation and convert to lowercase
    text = text.lower()
    text = ''.join([c for c in text if c.isalnum() or c.isspace()])

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Sort the word frequency dictionary by frequency in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_word_count