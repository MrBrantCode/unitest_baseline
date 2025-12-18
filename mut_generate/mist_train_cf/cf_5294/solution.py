"""
QUESTION:
Create a function named `contains_curse` that takes a sentence as input and returns `True` if the sentence contains any curse words from the `curse_words` list, and `False` otherwise. You cannot use the `in` operator or string matching methods such as `find()` or `index()` to check if a word is in the `curse_words` list. The comparison should be case-insensitive.
"""

def contains_curse(sentence):
    curse_words = ['curse1', 'curse2', 'curse3']  # replace with actual curse words

    # Split the sentence into a list of words
    words = sentence.split()

    # Iterate over each word in the sentence
    for word in words:
        # Iterate over each curse word in the curse_words list
        for curse_word in curse_words:
            # Compare the word with each curse word
            if word.lower() == curse_word.lower():
                return True

    return False