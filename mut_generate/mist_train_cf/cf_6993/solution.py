"""
QUESTION:
Create a function named `get_unique_words` that takes a string sentence as input. The function should return a list of unique words in the sentence, sorted by their frequency of occurrence in descending order. The function should handle punctuation marks, special characters, and numbers by removing them from the words and ignore the case of the words.
"""

def get_unique_words(sentence):
    frequency_count = {}

    words = sentence.split()
    for word in words:
        word = ''.join(e for e in word if e.isalnum()).lower()

        if word in frequency_count:
            frequency_count[word] += 1
        else:
            frequency_count[word] = 1

    sorted_words = sorted(frequency_count.items(), key=lambda x: x[1], reverse=True)
    unique_words = [word[0] for word in sorted_words]

    return unique_words