"""
QUESTION:
Create a function named `word_count` that takes a string of text as input and returns a dictionary where the keys are the words and the values are the number of times each word appears in the string. The function should consider case sensitivity and handle punctuation by removing it from the string before counting the words.
"""

def word_count(s):
    # Replacing punctuation
    s = s.replace('.', '').replace('?', '').replace('!', '').replace(',', '').replace(':', '').replace(';', '').replace('\'', '')

    counts = dict()
    words = s.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts