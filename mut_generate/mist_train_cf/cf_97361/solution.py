"""
QUESTION:
Create a function `sort_words_by_frequency` that takes a list of words as input and returns a list of words sorted by their frequency in descending order. If multiple words have the same frequency, they should be sorted alphabetically. If multiple words have the same frequency and are alphabetically sorted, they should be sorted in reverse order of length. The input list contains n words (1 <= n <= 10^5), where each word has at most m characters (1 <= m <= 100).
"""

def sort_words_by_frequency(words):
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    unique_words = sorted(set(words), key=lambda x: (-frequency_dict[x], x, -len(x)))
    sorted_words = []
    for word in unique_words:
        sorted_words.extend([word] * frequency_dict[word])
    return sorted_words