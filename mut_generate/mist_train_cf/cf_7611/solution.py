"""
QUESTION:
Create a function named `filter_words` that takes a list of words as input and returns a new list containing only the words that are at least 7 characters long and contain the letter 'a' or 'e' (case insensitive), sorted in reverse alphabetical order, with no duplicates, and limited to a maximum of 5000 words.
"""

def filter_words(words):
    filtered_words = []
    for word in words:
        if len(word) >= 7 and ('a' in word.lower() or 'e' in word.lower()):
            filtered_words.append(word.lower())

    filtered_words = list(set(filtered_words))
    filtered_words.sort(reverse=True)
    return filtered_words[:5000]  # limit the list to maximum 5000 words