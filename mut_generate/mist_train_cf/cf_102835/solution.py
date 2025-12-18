"""
QUESTION:
Create a function `create_frequency_chart` that takes a string of text as input and returns a dictionary where the keys are unique words from the text and the values are the frequency of each word. The function should count the occurrence of each word in the text, ignoring the case of the words and treating punctuation as part of the word.
"""

def create_frequency_chart(text):
    # Splitting the text into words
    words = text.split()

    # Creating an empty dictionary
    frequency_chart = {}

    # Counting the occurrence of each unique word
    for word in words:
        if word.lower() in frequency_chart:
            frequency_chart[word.lower()] += 1
        else:
            frequency_chart[word.lower()] = 1

    return frequency_chart