"""
QUESTION:
Create a function named `compare_word_sets_and_order` that takes two string parameters `phrase1` and `phrase2`. The function should return `True` if both phrases have the same words with the same frequency, in the same order, ignoring case and word repetition, and `False` otherwise.
"""

def compare_word_sets_and_order(phrase1, phrase2):
    """
    Ensure the two phrases have the exact same set of words, their order, and the frequency of each word, while ignoring word repetition and case
    """
    # Lowercase the phrases and split them into words
    words1 = phrase1.lower().split()
    words2 = phrase2.lower().split()

    # Construct dictionaries with words as keys and their frequencies as values
    freq_dict1 = {word: words1.count(word) for word in words1}
    freq_dict2 = {word: words2.count(word) for word in words2}

    # Compare the dictionaries
    if freq_dict1 != freq_dict2:
        return False

    # Check the order of the words
    for w1, w2 in zip(words1, words2):
        if w1 != w2:
            return False

    return True