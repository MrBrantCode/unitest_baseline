"""
QUESTION:
Create a function called `analyze_words` that takes a list of words as input. The function should return the longest word, the shortest word, the average word length, and a dictionary of character frequencies. The function should handle each string element as an array of characters and each character individually. 

Note: The list of words will only contain strings with lowercase letters.
"""

def analyze_words(words):
    """
    Analyzes a list of words and returns the longest word, shortest word, 
    average word length, and a dictionary of character frequencies.

    Args:
        words (list): A list of strings

    Returns:
        tuple: A tuple containing the longest word, shortest word, 
        average word length, and a dictionary of character frequencies.
    """

    # Initialize variables
    longest_word = words[0]
    shortest_word = words[0]
    length_sum = 0
    char_count = {}

    # Loop through the list
    for word in words:
        length = len(word)
        length_sum += length 

        # Check for longest and shortest words
        if length > len(longest_word):
            longest_word = word
        if length < len(shortest_word):
            shortest_word = word

        # Count character frequency
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # Compute average length
    avg_length = length_sum / len(words)

    return longest_word, shortest_word, avg_length, char_count