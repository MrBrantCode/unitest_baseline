"""
QUESTION:
Write a function `find_word_index(text, word)` that finds the index of the first occurrence of a given word within a text. The function should handle cases where the word is followed by punctuation marks or is part of a larger word. The search should be case-insensitive and consider the word as a whole, i.e., not as part of another word. Return the index of the first occurrence of the word, or -1 if the word is not found.
"""

def find_word_index(text, word):
    # Convert both the text and word to lowercase for case-insensitive comparison
    text = text.lower()
    word = word.lower()

    # Find the index of the word in the text
    index = text.find(word)

    # Handle cases where the word is followed by punctuation marks or is part of a larger word
    while index != -1:
        # Check if the word is at the start of the text or is preceded by a space
        if index == 0 or text[index - 1] == ' ':
            # Check if the word is at the end of the text or is followed by a punctuation mark or a space
            if index + len(word) == len(text) or text[index + len(word)] in (' ', ',', '.', '!', '?'):
                return index

        # Find the next occurrence of the word in the text
        index = text.find(word, index + 1)

    # Return -1 if the word is not found in the text
    return -1