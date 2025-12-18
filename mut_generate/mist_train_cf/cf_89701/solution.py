"""
QUESTION:
Create a function named `get_unique_words` that takes a sentence as input, removes any duplicate words, handles punctuation marks and special characters, and returns a list of unique words sorted by their frequency of occurrence in descending order. The function should be case-insensitive and ignore numbers.
"""

def get_unique_words(sentence):
    frequency_count = {}

    words = sentence.split()
    for word in words:
        word = ''.join(e for e in word if e.isalnum()).strip('.,!?()[]{}<>/\|@#$%^&*_~')
        word = word.lower()

        if word and not word.isdigit():
            if word in frequency_count:
                frequency_count[word] += 1
            else:
                frequency_count[word] = 1

    sorted_words = sorted(frequency_count.items(), key=lambda x: x[1], reverse=True)
    unique_words = [word[0] for word in sorted_words]

    return unique_words