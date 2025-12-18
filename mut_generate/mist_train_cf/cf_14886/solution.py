"""
QUESTION:
Create a function `sort_words_by_frequency` that takes a list of words as input, where the length of the list (n) is between 1 and 10^5, and the length of each word (m) is between 1 and 100. The function should return a list of unique words sorted by their frequency in descending order, and then alphabetically if multiple words have the same frequency. The time complexity should be better than O(n^2) and the space complexity should be better than O(n).
"""

def sort_words_by_frequency(words):
    word_frequency = {}
    
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    word_frequency_list = list(word_frequency.items())
    
    sorted_words = sorted(word_frequency_list, key=lambda x: (-x[1], x[0]))
    
    result = [word for word, _ in sorted_words]
    return result