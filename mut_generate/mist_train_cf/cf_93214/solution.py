"""
QUESTION:
Create a function named `filter_words` that takes a list of words as input. The input list should contain no more than 10 words and may be empty. The function should return a list of words that meet the following conditions: they have an even number of characters and contain no capital letters. The returned list should be sorted in descending order based on the length of the words.
"""

def filter_words(word_list):
    # Filter words with even length characters and no capital letters
    filtered_words = [word for word in word_list if len(word) % 2 == 0 and word.islower()]

    # Sort filtered words in descending order based on their length
    filtered_words.sort(key=len, reverse=True)

    return filtered_words