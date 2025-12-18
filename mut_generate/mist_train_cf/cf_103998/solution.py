"""
QUESTION:
Create a function `title_case(sentence)` that converts a given sentence to title case, where each word starts with a capital letter. The input sentence will only contain alphabetic characters and spaces. The function should return the title case sentence.
"""

def title_case(sentence):
    # Split the sentence into individual words
    words = sentence.split()

    # Convert the first character of each word to uppercase and the rest to lowercase
    title_words = [word[0].upper() + word[1:].lower() for word in words]

    # Join the title case words back into a sentence
    title_sentence = ' '.join(title_words)

    return title_sentence