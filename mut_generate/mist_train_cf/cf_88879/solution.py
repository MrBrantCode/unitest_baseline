"""
QUESTION:
Create a function named `contains_curse` that takes a sentence as input and returns `True` if the sentence contains any curse words and `False` otherwise. The function should not use the `in` operator or any string matching methods to check for curse words. The curse words are predefined in a list named `curse_words`. The function should be case-insensitive, treating 'curse1' and 'Curse1' as the same word.
"""

curse_words = ['curse1', 'curse2', 'curse3']  # replace with actual curse words

def contains_curse(sentence):
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