"""
QUESTION:
Create a function named `process_sentence` that takes a string as input. The function should remove punctuation, capitalize the first letter of each word, remove duplicate words, sort the words in alphabetical order, and count the number of times each word appears. The function should return the modified sentence, the sorted list of unique words, and a dictionary with the word count.
"""

def process_sentence(sentence):
    # Remove punctuation
    sentence = ''.join(e for e in sentence if e.isalnum() or e.isspace()).lower()

    # Split the sentence into words
    words = sentence.split()

    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]

    # Remove duplicate words
    unique_words = list(set(capitalized_words))

    # Sort the words in alphabetical order
    sorted_words = sorted(unique_words)

    # Count the number of times each word appears
    word_count = {}
    for word in capitalized_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Create the modified sentence
    modified_sentence = ' '.join(sorted_words)

    return modified_sentence, sorted_words, word_count