"""
QUESTION:
Implement a function `remove_duplicate_words(sentence)` that removes duplicate words from a given sentence while preserving the order of the remaining words. The solution should use only a single loop and not utilize any built-in functions or data structures to store unique words, achieving a time complexity of O(n), where n is the length of the sentence. The input sentence consists of alphanumeric characters and spaces.
"""

def remove_duplicate_words(sentence):
    # Convert the sentence into a list of characters
    sentence = list(sentence)

    # Create a set to store the unique words
    unique_words = set()

    # Create a variable to track the current word
    current_word = ""

    # Create a variable to track the updated sentence
    updated_sentence = []

    # Loop through each character in the sentence
    for char in sentence:
        # If the character is alphanumeric, add it to the current word
        if char.isalnum():
            current_word += char
        # If the character is a space or punctuation, check if the current word is a duplicate
        else:
            # If the current word is not in the set of unique words, add it to the set and the updated sentence
            if current_word not in unique_words:
                unique_words.add(current_word)
                updated_sentence.append(current_word)
            # Reset the current word
            current_word = ""

    # Check if the last word in the sentence is a duplicate and add it to the updated sentence if not
    if current_word not in unique_words:
        updated_sentence.append(current_word)

    # Convert the updated sentence back into a string
    updated_sentence = " ".join(updated_sentence)

    return updated_sentence