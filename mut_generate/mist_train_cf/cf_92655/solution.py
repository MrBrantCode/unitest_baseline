"""
QUESTION:
Write a function called `remove_duplicate_words` that takes a sentence as input and returns the sentence with all duplicate words removed while preserving the order of the remaining words. The function should use a single loop and no built-in data structures to store unique words, achieving a time complexity of O(n), where n is the length of the sentence. The input sentence consists of alphanumeric characters and spaces.
"""

def remove_duplicate_words(sentence):
    sentence = list(sentence)
    unique_words = set()
    current_word = ""
    updated_sentence = []

    for char in sentence:
        if char.isalnum():
            current_word += char
        else:
            if current_word not in unique_words:
                unique_words.add(current_word)
                updated_sentence.append(current_word)
            current_word = ""

    if current_word not in unique_words:
        updated_sentence.append(current_word)

    updated_sentence = " ".join(updated_sentence)
    return updated_sentence